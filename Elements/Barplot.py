import plotly.graph_objs as go


def barplot(data_x, data_y):
    data = [go.Bar(x=data_x, y=data_y)]
    layout = go.Layout(margin=dict(l=0, r=0, t=20, b=20), height=200)
    figure = go.Figure(data=data, layout=layout)
    return figure
