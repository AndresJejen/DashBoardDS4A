import plotly.graph_objs as go


def scatterplot(conversion, reference, since, to, event: str, title, x_title, y_title, height=300, mode='markers'):
    """
    Carga los datos y Layout de la grafica scatterplot
    :param conversion:
    :param reference:
    :param dates: Arreglo con las fechas
    :param since: Fecha de Inicio
    :param to: Fecha Final
    :return: Figure
    """
    data = [go.Scatter(x=reference, y=conversion, mode=mode)]
    layout = go.Layout(
        margin=dict(l=0, r=0, t=20, b=20),
        height=height,
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
