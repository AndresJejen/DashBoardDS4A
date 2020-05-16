from app import app, basic_data, es

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from Elements import card, lineplot, Dropdown, RangeSlider, scatterplot

topdates, events = basic_data

cards = dbc.Row([
            dbc.Col(card("card1", children="Historical conversions and event correlation"), width=4),
            dbc.Col(Dropdown("EventValues", "Events", events.Event.values), width=8)
        ])

historical_tab = html.Div([
    cards,
    dbc.Col(RangeSlider("rangeslider", topdates), width=11),
    dbc.Row([
        dbc.Col(html.Div(id="card3"), width=4),
        dbc.Col(html.Div(id="card4"), width=4),
        dbc.Col(html.Div(id="card5"), width=4)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='chart-with-slider'), width=4),
        dbc.Col(dcc.Graph(id='conversion_chart'), width=4),
        dbc.Col(dcc.Graph(id='correlation_chart'), width=4)
    ])
])


@app.callback(
    [
        Output('chart-with-slider', 'figure'),
        Output('conversion_chart', 'figure'),
        Output('correlation_chart', 'figure'),
        Output('card3', 'children'),
        Output('card4', 'children'),
        Output('card5', 'children'),
    ],
    [
        Input('rangeslider', 'value'),
        Input('EventValues', 'value')
    ]
)
def changerange_csv(year, event):
    evento = "conversion" if (event == "Events" or event is None) else event
    since, to = topdates.Date[year[0]], topdates.Date[year[1]]
    dates = es.gq_count_event_by_range(evento, since, to)
    dates_conversion = es.gq_count_event_by_range("conversion", since, to)

    figure_lineplot = lineplot(dates, since, to, evento)
    conversion_lineplot = lineplot(dates_conversion, since, to, 'conversion')
    correlation_scatter = scatterplot(dates_conversion.Total, dates.Total, since, to, 'conversion')

    return [figure_lineplot, conversion_lineplot, correlation_scatter, evento, "Conversion", "Scatter Plot"]
