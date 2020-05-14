import dash_core_components as dcc

def RangeSlider(id, topdates):
    return dcc.RangeSlider(
        id=id,
        min=topdates.index[0],
        max=topdates.index[-1],
        step=1,
        value=[topdates.index[0], topdates.index[-1]],
        marks={numd: date.strftime('%d-%m-%Y') for numd, date in zip(topdates.index, topdates['Date']) if numd % 30 == 0}
    )