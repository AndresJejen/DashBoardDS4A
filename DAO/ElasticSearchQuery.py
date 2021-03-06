from elasticsearch import Elasticsearch, RequestsHttpConnection, helpers
import pandas as pd


class ElasticSearchQuery:
    """
    Class that abstract the Complexity of Elasticsearch SDK
    """

    def __init__(self, user: str, password: str, url: str):
        """
        Creates a object of DAO
        :param user:
        :param password:
        :param url:
        """
        self.user = user
        self.password = password
        self.url = url
        self.try_connect()

    def try_connect(self):
        """
        Generates the Conection to Elastic Search
        :return:
        """
        self.es = Elasticsearch(
            hosts=[{'host': self.url, 'port': 443}],
            http_auth=(self.user, self.password),
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection
        )

    def send_query(self, query):
        """
        Execute the Query to Elastic Search
        :param query:
        :return:
        """
        return self.es.search(index="ds4adate", body=query)

    def gq_max_min_timestamp(self):
        """
        Query Min and Max Date on Data
        :return:
        """
        query = {
          "size": 0,
          "aggs": {
            "Min": {
              "min": {"field": "timestamp"}
            },
            "Max": {
              "max": {"field": "timestamp"}
            }
          }
        }
        dates = self.send_query(query)
        min = dates["aggregations"]['Min']['value_as_string']
        max = dates["aggregations"]['Max']['value_as_string']
        return pd.DataFrame(pd.date_range(start=min, end=max),columns=["Date"])

    def gq_count_event_by_range(self, event: str, startdate: str, enddate: str, range: str = "day"):
        """
        Query a list of the count by dat of an event
        :param event:
        :param startdate:
        :param enddate:
        :param range:
        :return:
        """
        query = {
          "size": 0,
          "query": {
              "bool": {
                "must": [
                  {
                    "match": {"event": event}
                  }
                ],
                "filter": [
                  {
                     "range" : {
                        "timestamp": {
                              "gte": "{}".format(startdate),
                              "lt":  "{}".format(enddate)
                          }
                      }
                  }
                ]
              }
          },
          "aggs": {
                "sales_over_time" : {
                    "date_histogram": {
                        "field": "timestamp",
                        "calendar_interval": range
                    }
                }
            }
        }
        data = self.send_query(query)
        data = pd.DataFrame(data['aggregations']['sales_over_time']['buckets'])
        data.columns = ["Date", "key", "Total"]
        data.index = data.Date.values
        data.drop(["Date"], inplace=True, axis=1)
        data.index = pd.to_datetime(data.index)
        return data

    def gq_all_dates_dataframe(self):
        """
        Query A list of all the Dates
        :return:
        """
        query = {
            "size": 0,
            "aggs": {
                "All Dates": {
                    "date_histogram": {
                        "field": "timestamp",
                        "calendar_interval": "day"
                    }
                }
            }
        }
        dataframe = pd.DataFrame(self.send_query(query)["aggregations"]["All Dates"]["buckets"])
        dataframe['key_as_string'] = pd.to_datetime(dataframe['key_as_string'])
        return dataframe

    def gq_all_events_dataframe(self):
        """
        Query a list of unique events
        :return:
        """
        query = {
            "size": 0,
            "aggs": {
                "Eventos": {
                    "terms": {
                        "field": "event.keyword",
                        "size": 50
                    }
                }
            }
        }
        data = self.send_query(query)["aggregations"]["Eventos"]["buckets"]
        data = pd.DataFrame(data)
        data.columns = ["Event", "Total"]
        return data

    def gq_prices_in_conversions(self, startdate: str, enddate: str):
        """
        Query of prices in conversions
        :param startdate:
        :param enddate:
        :return:
        """
        query = {
              "_source": "price",
              "query": {
                  "bool": {
                    "must": [
                      {
                        "match": {"event": "conversion"}
                      }
                    ],
                    "must_not": [
                      {"term": {
                        "price": {
                          "value": "undefined"
                        }
                      }}
                    ],
                    "filter": [
                      {
                         "range" : {
                            "timestamp": {
                                  "gte": "{}".format(startdate),
                                  "lt":  "{}".format(enddate)
                              }
                          }
                      }
                    ]
                  }
              }
            }
        data = self.send_query(query)["hits"]["hits"]
        data = map(lambda x: x['_source'], data)
        data = pd.DataFrame(data)
        data.price = data.price.apply(lambda x: float(x))
        return data

    def gq_num_convertions_by_person(self, startdate: str, enddate: str):
        """
        Query all conversions by person
        :param startdate:
        :param enddate:
        :return:
        """
        query = {
          "size": 0,
          "query": {
              "bool": {
                "must": [
                  {
                    "match": {"event": "conversion"}
                  }
                ],
                "filter": [
                  {
                     "range" : {
                        "timestamp": {
                              "gte": "{}".format(startdate),
                              "lt":  "{}".format(enddate)
                          }
                      }
                  }
                ]
              }
          },
          "aggs": {
                "convertions": {
                    "terms": {
                        "field": "person.keyword",
                        "size": 10000
                    }
                }
            }
        }
        data = self.send_query(query)["aggregations"]["convertions"]['buckets']
        data = pd.DataFrame(data)
        data.columns = ["person", "Total Purchases"]
        return data

    def gq_personpurchase_conversion(self, startdate: str, enddate: str):
        """
        Query all person purchase conversion
        :param startdate:
        :param enddate:
        :return:
        """
        query = {
          "_source": ["person-purchase"],
          "query": {
              "bool": {
                 "must": [
                  {
                    "match": {"event": "conversion"}
                  }
                ],
                "filter": [
                  {
                     "range" : {
                        "timestamp": {
                              "gte": "{}".format(startdate),
                              "lt":  "{}".format(enddate)
                          }
                      }
                  }
                ]
              }
          }
        }
        person_purchase = self.send_query(query)["hits"]["hits"]
        person_purchase = map(lambda x: x['_source'], person_purchase)
        person_purchase = pd.DataFrame(person_purchase)
        return person_purchase

    def gq_count_model_purchases(self, startdate: str, enddate: str):
        """
        Query a count of purchases by model
        :param startdate:
        :param enddate:
        :return:
        """
        query = {
          "size": 0,
          "query": {
            "bool": {
              "must": [
                {
                  "match": {
                    "event": "conversion"
                  }
                }
              ],
              "filter": [
                {
                   "range" : {
                      "timestamp": {
                            "gte": "{}".format(startdate),
                            "lt":  "{}".format(enddate)
                        }
                    }
                }
              ]
            }
          },
          "aggs": {
            "countByBrand": {
              "terms": {
                "field": "model.keyword",
                "size": 1000
              }
            }
          }
        }
        model_purchase = self.send_query(query)["aggregations"]["countByBrand"]['buckets']
        model_purchase = pd.DataFrame(model_purchase)
        model_purchase.key = model_purchase.key.apply(lambda x: x.split(" ")[0])
        model_purchase = model_purchase.groupby('key').sum().sort_values(by=["doc_count"], ascending=True).reset_index()
        model_purchase.columns = ["Brand", "Total"]
        return model_purchase

    def gq_count_condition_purchases(self, startdate: str, enddate: str):
        """
        Query a count of conversions by condition by date range
        :param startdate:
        :param enddate:
        :return:
        """
        query = {
          "size": 0,
          "query": {
            "bool": {
              "must": [
                {
                  "match": {
                    "event": "conversion"
                  }
                }
              ],
              "filter": [
                {
                   "range" : {
                      "timestamp": {
                            "gte": "{}".format(startdate),
                            "lt":  "{}".format(enddate)
                        }
                    }
                }
              ]
            }
          },
          "aggs": {
            "countBycondition": {
              "terms": {
                "field": "condition.keyword",
                "size": 1000
              }
            }
          }
        }
        condition_purchase = self.send_query(query)["aggregations"]["countBycondition"]['buckets']
        condition_purchase = pd.DataFrame(condition_purchase)
        condition_purchase = condition_purchase.sort_values(by=["doc_count"], ascending=True).reset_index(drop=True)
        condition_purchase.columns = ["Brand", "Total"]
        return condition_purchase
