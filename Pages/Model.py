from app import app, basic_data, es, modelo

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from Elements import Histogram, RangeSlider, barplot

import numpy as np

cards = dbc.Row([
            dbc.Col(html.H2("Model"), width=9)
        ])

numeric_fields = ["Price", "Past purchases", "Hours elapsed", "Activity count", "num Sessions"]
categorical_fields = [
    {
        "Label": "Condition",
        "Options": ["Bom", "Bom - Sem Touch ID", "Excelente", "Muito Bom", "Novo"] # 5
    },
    {
        "Label": "Storage",
        "Options": ["128GB", "16GB", "1TB", "256GB", "32GB", "32GB RAM 2GB", "32GB RAM 3GB", "4GB", "512GB", "512MB", "64GB", "64GB RAM:4GB", "64GB RAM:6GB", "8GB"] #14
    },
    {
        "Label": "Brand",
        "Options": ["Asus", "Huawei", "LG", "Lenovo", "Motorola", "Multilaser", "Positivo", "Quantum", "Samsung", "Sony", "Xiaomi", "iPad", "iPhone"] # 13
    }]


fields = [{"Label": field, "type": "number"} for field in numeric_fields]
fields_categorical = [{"Label": field['Label'], "Options": field["Options"], "type": "select",} for field in categorical_fields]

fields_list = [html.Td(dbc.Input(id="input_{}".format(field['Label']), placeholder=field['Label'], type=field["type"])) for field in fields]

def create_select(field):
    return dbc.Select(id="input_{}".format(field['Label']), options=[{"label": option, "value": key} for key, option in enumerate(field['Options'])])

fields_list = fields_list + [html.Td(create_select(field)) for field in fields_categorical]

row = html.Tr(fields_list)

table_header = [
    html.Thead(html.Tr([html.Th(title["Label"]) for title in fields+fields_categorical]))
]

table_body = [html.Tbody([row])]

model_tab = html.Div([
    cards,
    dbc.Table(table_header + table_body),
    html.Div(id="Hola1", children="Hola1")
])


@app.callback(
    [
        Output('Hola1', 'children'),
    ],
    [Input("input_{}".format(field['Label']), 'value') for field in fields+fields_categorical]
)
def predictProbaModel(*args):
    """
    Callback when a field is updated
    :param args:
    :return:
    """
    predicted = None
    any_null = validateNone(args)
    if (any_null):
        fields = transformFields(args[-3:])
        fields = list(args[0:5]) + fields
        predicted = testModel(fields)
    return [predicted]

def validateNone(array):
    """
    Valida si los campos Estan Bien Diligenciados
    :param array:
    :return:
    """
    for i in array:
        if (i == None):
            return False
    return True

def testModel(parameters):
    """
    Ejecita el Modelo Random Forest
    :param parameters:
    :return:
    """
    return modelo.predict_proba([parameters])

def transformFields(categoricals):
    """
    Transforma los campos categoricos a One Hot
    :param fields:
    :return:
    """
    total = [4, 13, 12]
    converted = []
    for key, field in enumerate(categoricals):
        value = int(field)
        temp = list(np.zeros(total[key]))
        if (value != 0):
            temp[value-1] = 1
        converted = converted + temp
    return converted
