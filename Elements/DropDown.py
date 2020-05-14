import dash_bootstrap_components as dbc
import dash_core_components as dcc

def Dropdown(id, value, list):
    return dcc.Dropdown(
        id=id,
        value=value,
        options=[
            {"label": item, "value": item} for item in list
        ]
    )
