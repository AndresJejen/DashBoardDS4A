import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


cards = dbc.Row([
            html.H1(children='Introduction')
        ])

col_width = 6

introduction_tab = html.Div([
    cards,
    dbc.Row([
        dbc.Col(
            [
                dbc.Row(
                    html.H2("Company Objective", style={"text-decoration": "underline"}, className='mt-5 mb-5')
                ),
                dbc.Row(
                    html.Ul([
                        html.Li("Improve company conversion"),
                        html.Li("Reduce CAC"),
                        html.Li(html.B("Make 'offers' to undecided* clients")),
                    ])
                ),
                dbc.Row(
                    html.H2("Model Objective", style={"text-decoration": "underline"}, className='mt-5 mb-5')
                ),
                dbc.Row(
                    html.Ul([
                        html.Li([
                            html.B("Main: "),
                            "Calculate purchase probability"
                        ]),
                        html.Li([
                            html.B("Secondary: "),
                            "Predict binary class (0,1)"
                        ]),
                        html.Li(html.B("Make 'offers' to undecided* clients")),
                    ])
                ),
                dbc.Row(
                    html.H6("* Undecided = Medium probability to purchase", className='mt-5 mb-5')
                ),
            ], width=6),
        dbc.Col(
            [
                dbc.Row(
                    html.H2("Methodology", style={"text-decoration": "underline"}, className='mt-5 mb-3')
                ),
                dbc.Row(
                    html.Ul([
                        html.Li("Random forest classifier"),
                        html.Li(
                            [
                                html.B("Input"),
                                "Relevant features, mostly related to past activity"
                            ]
                        ),
                        html.Li(
                            [
                                html.B("Output"),
                                "Purchase probability and class prediction"
                            ]
                        ),
                        html.Li(
                            [
                                html.B("Threshold: 35% "),
                                "due to imbalanced dataset"
                            ]
                        )
                    ])
                ),
                dbc.Row(
                    html.H2("Tab Guide", style={"text-decoration": "underline"}, className='mt-5 mb-3')
                ),
                dbc.Row(
                    html.Ul([
                        html.Li([
                            html.B("General: "),
                            "Some general conversion data"
                        ]),
                        html.Li([
                            html.B("Correlation: "),
                            "Analysis to calculate past vs. purchases"
                        ]),
                        html.Li([
                            html.B("Model: "),
                            "Random forest model based on inputs defined"
                        ]),
                    ])
                ),
                dbc.Row(
                    html.H5("Main takeaway is if we should make an extra push with client if they are undecided", className='mt-5 mb-5')
                ),
            ],
            width=6)
    ])
])
