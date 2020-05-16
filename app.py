import dash
import dash_bootstrap_components as dbc
from DAO.ElasticSearchQuery import ElasticSearchQuery

styles = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=styles)
server = app.server
app.config.suppress_callback_exceptions = True

user = 'Andres'
password = 'Andres123*'
url = "search-ds4a1-ewn5ngrlak4w5vxytn4h3h54za.us-east-1.es.amazonaws.com"
es = ElasticSearchQuery(user, password, url=url)

basic_data = [es.gq_max_min_timestamp(), es.gq_all_events_dataframe()]
