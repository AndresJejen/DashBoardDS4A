import dash_core_components as dcc
import dash_html_components as html


def RangeSlider(id, topdates):
    return html.Div([
        html.H5("Date Range Selector"),
        dcc.RangeSlider(
            id=id,
            min=topdates.index[0],
            max=topdates.index[-1],
            step=1,
            value=[topdates.index[0], topdates.index[-1]],
            marks={numd: date.strftime('%d-%m-%Y') for numd, date in zip(topdates.index, topdates['Date']) if numd % 45 == 0},
        ),
        html.Div(id='output-{}'.format(id))
    ], style={'margin': '5% auto', 'padding': 'auto'})
