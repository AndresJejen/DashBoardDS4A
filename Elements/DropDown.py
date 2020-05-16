import dash_core_components as dcc


def Dropdown(id: str, value: str = "conversion", list = []):
    """
    Genera un dropDown
    :param id:
    :param value:
    :param list:
    :return:
    """
    return dcc.Dropdown(
        id=id,
        value=value,
        options=[
            {"label": item, "value": item} for item in list
        ]
    )
