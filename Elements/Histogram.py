import plotly.graph_objs as go


def Histogram(data):
    data = [go.Histogram(x=data, nbinsx=20)]
    layout = go.Layout(margin=dict(l=0, r=0, t=20, b=20), height=200)
    figure = go.Figure(data=data, layout=layout)
    return figure
