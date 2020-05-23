import dash
import dash_bootstrap_components as dbc
from DAO.ElasticSearchQuery import ElasticSearchQuery
from Models.ProjectModel import ProjectModel
import os
from pathlib import Path  # python3 only
from dotenv import load_dotenv

# OR, explicitly providing path to '.env'
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Server configuration
styles = [dbc.themes.SIMPLEX]
app = dash.Dash(__name__, external_stylesheets=styles)
server = app.server
app.config.suppress_callback_exceptions = True

# Connection Settings
user = os.getenv('ES_USER')
password = os.getenv('ES_PASS')
url = os.getenv('ES_URL')
es = ElasticSearchQuery(user, password, url=url)

# Basic Data for common pages
basic_data = [es.gq_max_min_timestamp(), es.gq_all_events_dataframe()]

# Random Forest Model
modelo = ProjectModel()





