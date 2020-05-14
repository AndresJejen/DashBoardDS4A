import dash_bootstrap_components as dbc
import dash_html_components as html


def card(id):
    return dbc.Card(
        dbc.CardBody(
            [
                html.H5(id =id, children="Card title", className="card-title"),
            ]
        )
    )