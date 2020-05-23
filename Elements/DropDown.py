import dash_core_components as dcc
import dash_html_components as html


def Dropdown(id: str, value: str = "conversion", list = []):
    """
    Genera un dropDown
    :param id:
    :param value:
    :param list:
    :return:
    """
    return html.Div([
        html.H5("Event Selector"),
        dcc.Dropdown(
            id=id,
            value=value,
            options=[
                {"label": item, "value": item} for item in list
            ]
        ),
        html.Div(id='output-{}'.format(id))
    ], style={'margin': '5% auto', 'padding': 'auto'})
