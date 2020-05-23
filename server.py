from app import app, es

import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from Pages import historical_tab, general_tab, model_tab

cards = dbc.Row([
            dbc.Col(html.H1("Trocafone DashBoard DS4A"), width=10),
        ])

tabs = dbc.Tabs(
    [
        dbc.Tab(label="General", tab_id="General"),
        dbc.Tab(label="Historical", tab_id="Historical"),
        dbc.Tab(label="Model", tab_id="Model"),
    ],
    id="tabs",
)

app.layout = dbc.Container([
                cards,
                tabs,
                html.Div(id="tab-content", className="p-4")
            ])


@app.callback(
    Output("tab-content", "children"),
    [Input("tabs", "active_tab")],
)
def render_tab_content(active_tab):
    """
    Renderiza el contenido de los Tabs
    :param active_tab:
    :return:
    """
    if active_tab is not None:
        if active_tab == "Historical":
            return historical_tab
        if active_tab == "General":
            return general_tab
        if active_tab == "Model":
            return model_tab
    return historical_tab


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
