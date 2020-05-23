from app import app, basic_data, es

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from Elements import lineplot, Dropdown, RangeSlider, scatterplot

from Models import LinearRegressionModel
from ProcesingData import concat

# General App Data
topdates, events = basic_data

# Ids
sliderId = "rangeslider"

cards = dbc.Row([
            dbc.Col(html.H2("Historical conversions and event correlation"), width=9)
        ])

historical_tab = html.Div([
    cards,
    dbc.Row([
        dbc.Col(RangeSlider(sliderId, topdates), width=10),
        dbc.Col(Dropdown("EventValues", "visited site", events.Event.values), width=2)
    ],align="baseline"),
    dbc.Row([
        dbc.Col(html.Div(id="card3"), width=4),
        dbc.Col(html.Div(id="card4"), width=4),
        dbc.Col(html.Div(id="card5"), width=4)
    ], className="h-25"),
    dbc.Row([
        dbc.Col(dcc.Graph(id='chart-with-slider'), width=4),
        dbc.Col(dcc.Graph(id='conversion_chart'), width=4),
        dbc.Col([
            dbc.Row(
                dbc.Col(dcc.Graph(id='correlation_chart'))
            ),
            dbc.Row([
                    dbc.Col(html.Div(id="HistoricalScore", children="")),
                    dbc.Col(html.Div(id="HistoricalCoef", children="")),
                    dbc.Col(html.Div(id="HistoricalCorr", children=""))
            ])], width=4)
    ],align="stretch")])


@app.callback(
    [
        Output('chart-with-slider', 'figure'),
        Output('conversion_chart', 'figure'),
        Output('correlation_chart', 'figure'),
        Output('card3', 'children'),
        Output('card4', 'children'),
        Output('card5', 'children'),
        Output('output-{}'.format(sliderId), 'children'),
        Output('HistoricalScore', 'children'),
        Output('HistoricalCoef', 'children'),
        Output('HistoricalCorr', 'children'),
    ],
    [
        Input(sliderId, 'value'),
        Input('EventValues', 'value')
    ]
)
def changerange_csv(year, event):
    event = event if event is not None else "visited site"
    since, to = topdates.Date[year[0]], topdates.Date[year[1]]

    dates = es.gq_count_event_by_range(event, since, to)
    dates_conversion = es.gq_count_event_by_range("conversion", since, to)

    figure_lineplot = lineplot(dates.index, dates['Total'], since, to, event)
    conversion_lineplot = lineplot(dates_conversion.index, dates_conversion['Total'], since, to, 'conversion')
    correlation_scatter = scatterplot(dates_conversion.Total, dates.Total, since, to, 'conversion')

    visits_vs_purchases = concat(dates, dates_conversion, axis=1, columns=["key", "events", "key_2", "conversion"])
    visits_vs_purchases = visits_vs_purchases.dropna()
    score, coef, _ = LinearRegressionModel(visits_vs_purchases.events, visits_vs_purchases.conversion)
    corr = visits_vs_purchases.corr().iloc[1, 3]

    return [figure_lineplot,
            conversion_lineplot,
            correlation_scatter,
            event,
            "Conversion",
            "Scatter Plot",
            'You have selected " From {0:%Y-%m-%d} - To {1:%Y-%m-%d}"'.format(since, to),
            "R-Score: \t{:.3f}".format(score), "Coeficient: \t{:.3f}".format(coef[0, 0]), "Correlation: \t{:.3f}".format(corr)
            ]
