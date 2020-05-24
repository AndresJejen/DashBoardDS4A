from app import app, modelo

import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from Elements import dash_table
import numpy as np
from Pages.StaticModelPageData import fields, fields_categorical, example_data

cards = dbc.Row([
            dbc.Col(html.H2("Model"), width=10),
            dbc.Col(dbc.Button(id="ExampleButton", children="Show Example", color="success", className="mr-1"), width=2)
        ])

model_tab = html.Div([
    cards,
    dash_table(fields, fields_categorical),
    dbc.Row([
        dbc.Col([
            dbc.Row(
                html.H3("Purchase Probability", style={"margin": "auto", "text-decoration": "underline"}),
                className="h-25"
            ),
            dbc.Row(
                html.H1(id="Probability", children="Random Forest", style={"margin": "auto"}),
                className="h-25",
                style={"text-align": "center"}
            ),
            dbc.Row(
                html.H3(
                    children="Predicted class - Threshold 35%",
                    style={"margin": "auto", "text-decoration": "underline"}
                ),
                className="h-25"
            ),
            dbc.Row(
                html.H2(
                    id="Conversion",
                    children="Converts",
                    style={"margin": "auto"}
                )
            ),
        ], width=4),
        dbc.Col([
            dbc.Row(
                html.H3("Potential Actions", style={"margin": "auto", "text-decoration": "underline"}),
                className="h-25"
            ),
            dbc.Row(
                [
                    dbc.Col(width=1),
                    dbc.Col([
                        dbc.Row(
                            html.H5(id="range1", children="0% - 20%\t Low Purchase Probability - Non costly actions"),
                            className="h-25"
                        ),
                        dbc.Row(
                            html.H5(
                                id="range2",
                                children="20% - 35%\t Potential Actions - coupons, discounts, credit for future purchases, etc."),
                            className="h-25"
                        ),
                        dbc.Row(
                            html.H5(
                                id="range3",
                                children="35% - 100%\t High purchase probability - Non costly actions"),
                            className="h-25"
                        ),
                        dbc.Row(
                            className="h-25"
                        ),
                    ], width=11)
                ],
                className="h-75"
            )
        ], width=8)
    ], className="h-100")
], style={"height": "300px"})


@app.callback(
    [
        Output('Probability', 'children'),
        Output('Conversion', 'children')
    ] + [Output(f'range{range_value}', 'style') for range_value in [1, 2, 3]] + [Output('Conversion', 'style')],
    [Input("input_{}".format(field['Label']), 'value') for field in fields + fields_categorical]
)
def predict_probability_model(*args):
    """
    Callback when a field is updated
    :param args: list of values from inputs
    :return: Array with Data for every Output
    """
    final_data = None
    any_null = validate_none(args)
    if any_null:
        final_data = transform_fields(args[-3:])
        final_data = list(args[0:5]) + final_data
    predicted = test_model(final_data)
    converts, styles = user_converts(predicted)

    return [f'{predicted} %', converts] + styles


@app.callback(
    [Output("input_{}".format(field['Label']), 'value') for field in fields + fields_categorical],
    [Input("ExampleButton", "n_clicks")]
)
def on_button_click(n):
    """
    Apply some prefixed example
    :param n:
    :return:
    """
    example = np.random.randint(4, size=(1, 1))
    return example_data[example[0][0]]


def user_converts(predicted_value):
    """
    Converts the predicted value into text and styles for easy visualization
    :param predicted_value:
    :return:
    """
    style = {"border-radius": "20px", "padding": "10px", "vertical-align": "middle", "margin": "auto"}

    if predicted_value == 'No Value':
        return "No Value", [style]*4
    elif predicted_value < 20:
        selected_style = {**style, **{"background-color": "red", "color": "white"}}
        return "NO", [selected_style, style, style, selected_style]
    elif (predicted_value >= 20) and (predicted_value < 35):
        selected_style = {**style, **{"background-color": "yellow", "color": "black"}}
        return "Undecided, needs push", [style, selected_style , style, selected_style]
    else:
        selected_style = {**style, **{"background-color": "green", "color": "white"}}
        return "Yes", [style, style, selected_style, selected_style]


def validate_none(value_inputs):
    """
    Validation of inputs
    :param value_inputs: List of values from Input controls
    :return:
    """
    for inputValue in value_inputs:
        if inputValue is None:
            return False
    return True


def test_model(parameters):
    """
    Predict the probability using the fields from inputs
    :param parameters: List of data uses to predict
    :return:
    """
    if parameters is None:
        return "No Value"
    else:
        return round(modelo.predict_proba([parameters])[0]*100, 3)


def transform_fields(categorical_fields):
    """
    Transform the categorical data into One Hot Encoding
    :param categorical_fields: List of values from categorical fields
    :return:
    """
    total = [4, 13, 12]
    converted = []
    for key, field in enumerate(categorical_fields):
        value = int(field)
        temp = list(np.zeros(total[key]))
        if value is not 0:
            temp[value - 1] = 1
        converted = converted + temp
    return converted
