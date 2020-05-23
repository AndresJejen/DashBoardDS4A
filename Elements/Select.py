import dash_bootstrap_components as dbc


def create_select(field):
    """
    Create Select Field
    :param field:
    :return:
    """
    return dbc.Select(
        id="input_{}".format(field['Label']),
        options=[
            {
                "label": option,
                "value": key
            } for key, option in enumerate(field['Options'])
        ])
