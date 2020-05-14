from elasticsearch import Elasticsearch, RequestsHttpConnection, helpers
import pandas as pd
import json


class ElasticSearchQuery:
    """
    Class that abstract the Complexity of Elasticsearch SDK
    """

    def __init__(self, user: str, password: str, url: str):
        self.user = user
        self.password = password
        self.url = url
        self.try_connect()

    def try_connect(self):
        """
        Generates the COnection to Elastic Search
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
        data.columns = ["Date","key","Total"]
        data.Date = pd.to_datetime(data.Date)
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
