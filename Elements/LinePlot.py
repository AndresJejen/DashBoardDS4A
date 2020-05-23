import plotly.graph_objs as go


def lineplot(x, y, since, to, event: str, height = 300):
    """
    Carga los datos y Layout de la grafica lineplot
    :param dates: Arreglo con las fechas
    :param since: Fecha de Inicio
    :param to: Fecha Final
    :return: Figure
    """
    data = [go.Scatter(x=x, y=y)]
    layout = go.Layout(margin=dict(l=0, r=0, t=20, b=20), height=height)
    figure = go.Figure(data=data, layout=layout)
    return figure
