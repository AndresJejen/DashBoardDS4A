import plotly.graph_objs as go


def Histogram(data, title, x_title, y_title):
    """
    Creates a histogram
    :param data:
    :param title:
    :param x_title:
    :param y_title:
    :return:
    """
    data = [go.Histogram(x=data, nbinsx=20)]
    layout = go.Layout(
        margin=dict(l=0, r=0, t=20, b=20),
        height=200,
        title=title,
        xaxis={
            'title': x_title
        },
        yaxis={
            'title': y_title
        }
    )
    figure = go.Figure(data=data, layout=layout)
    return figure
