import plotly.graph_objs as go


def lineplot(dates, since, to, event: str):
    """
    Carga los datos y Layout de la grafica lineplot
    :param dates: Arreglo con las fechas
    :param since: Fecha de Inicio
    :param to: Fecha Final
    :return: Figure
    """
    data = [go.Scatter(x=dates['Date'], y=dates['Total'])]
    layout = go.Layout(margin=dict(l=0, r=0, t=20, b=20),)
    figure = go.Figure(data=data, layout=layout)
    return figure
