import plotly.graph_objs as go


def barplot(data_x, data_y, title, x_title, y_title):
    """
    Creates a bar plot
    :param data_x: Data of Axis X
    :param data_y: Data of axis Y
    :param title: Title of plot
    :param x_title: Title of axis x
    :param y_title: Title of axis y
    :return:
    """
    data = [go.Bar(x=data_y, y=data_x, orientation='h')]
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
