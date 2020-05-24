from app import app, basic_data, es

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from Elements import Histogram, RangeSlider, barplot

# Datos Generales
topdates = basic_data[0]

# Ids
sliderId = "rangeSliderGeneral"

cards = dbc.Row([
            html.H1(children='General Overview')
        ])

col_width=6

general_tab = html.Div([
    cards,
    dbc.Col(RangeSlider(sliderId, topdates), width=12),
    dbc.Row([
        dbc.Col(html.H4("Quantity and price distribution"), style={"text-align": "center"}, width=col_width),
        dbc.Col(html.H4("Purchase Description"), style={"text-align": "center"}, width=col_width)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='histogram-prices-conversion'), width=col_width, style={"margin": "auto"}),
        dbc.Col(dcc.Graph(id='barplot-brand-conversion'), width=col_width, style={"margin": "auto"}),
    ], style={"margin-top": "5px"}),
    dbc.Row([
        dbc.Col(dcc.Graph(id='histogram-number-person-conversion'), width=col_width, style={"margin": "auto"}),
        dbc.Col(dcc.Graph(id='barplot-condition-conversion'), width=col_width, style={"margin": "auto"}),
    ], style={"margin-top": "10px"})
])


@app.callback(
    [
        Output('histogram-prices-conversion', 'figure'),
        Output('histogram-number-person-conversion', 'figure'),
        Output('barplot-brand-conversion', 'figure'),
        Output('barplot-condition-conversion', 'figure'),
        Output('output-{}'.format(sliderId), 'children')
    ],
    [
        Input(sliderId, 'value')
    ]
)
def changerange_csv(year):
    since, to = topdates.Date[year[0]], topdates.Date[year[1]]

    datos_prices_conversion = es.gq_prices_in_conversions(since, to)
    datos_person_conversion = es.gq_num_convertions_by_person(since, to)
    datos_brand_conversion = es.gq_count_model_purchases(since, to)
    datos_condition_conversion = es.gq_count_condition_purchases(since, to)

    prices_conversion = Histogram(datos_prices_conversion['price'], "Number of conversions by groups of Prices by Day", "Price", "# of conversions")
    person_conversion = Histogram(datos_person_conversion['Total Purchases'], "Number of conversions by groups of Persons by Day", "Person", "# of conversions")
    brand_conversion = barplot(datos_brand_conversion['Brand'], datos_brand_conversion['Total'], "Number of conversions by Brand in range of time", "# of conversions", "Brands")
    condition_conversion = barplot(datos_condition_conversion['Brand'], datos_condition_conversion['Total'], "Number of conversions by Quality status of device in range of time", "# of conversions", "Quality status")

    return [prices_conversion,
            person_conversion,
            brand_conversion,
            condition_conversion,
            'You have selected " From {0:%Y-%m-%d} - To {1:%Y-%m-%d}"'.format(since, to)]
