import dash_bootstrap_components as dbc
import dash_html_components as html
from Elements.Select import create_select


def dash_table(fields, fields_categorical):
    """
    Creates the table with the controls where user can add
    values to prediction
    :param fields:
    :param fields_categorical:
    :return:
    """
    fields_list = [
        html.Td(dbc.Input(id="input_{}".format(field['Label']), placeholder=field['Label'], type=field["type"])) for
        field in fields]

    fields_list = fields_list + [html.Td(create_select(field)) for field in fields_categorical]

    row = html.Tr(fields_list)

    table_header = [
        html.Thead(
            html.Tr(
                [
                    html.Th(
                        [
                            html.P(
                                id=f'head_{key}',
                                children=title['Label']
                            ),
                            dbc.Tooltip(
                                title['Description'],
                                target=f"head_{key}",
                            ),
                        ]
                    ) for key, title in enumerate(fields + fields_categorical)
                ]
            )
        )
    ]

    table_body = [html.Tbody([row])]
    return dbc.Table(table_header + table_body)


