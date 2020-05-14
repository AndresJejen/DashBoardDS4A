from app import app, es

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from Elements.Cards import card
from Elements.LinePlot import lineplot
from Elements.DropDown import Dropdown
from Elements.Slider import RangeSlider


topdates = es.gq_max_min_timestamp()
events = es.gq_all_events_dataframe()

cards = dbc.Row([dbc.Col(card("card1"), width=4), dbc.Col(card("card2"), width=8)])
app.layout = html.Div([
    cards,
    RangeSlider("rangeslider", topdates),
    Dropdown("EventValues", "Events",events.Event.values),
    dcc.Graph(id='chart-with-slider'),
])


@app.callback(
    [Output('chart-with-slider', 'figure')],
    [
        Input('rangeslider', 'value'),
        Input('EventValues', 'value')
    ]
)
def changeRange_csv(year, evento):
    evento = "conversion" if evento == "Events" else evento
    since, to = topdates.Date[year[0]], topdates.Date[year[1]]
    dates = es.gq_count_event_by_range(evento, since, to)

    figure_lineplot = lineplot(dates,since, to, evento)

    return [figure_lineplot]

if __name__ == '__main__':
    app.run_server(debug=True)
