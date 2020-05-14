import plotly.graph_objs as go


def lineplot(dates, since, to, evento):
    """
    Carga los datos y Layout de la grafica lineplot
    :param dates: Arreglo con las fechas
    :param since: Fecha de Inicio
    :param to: Fecha Final
    :return: Figure
    """
    data = [go.Scatter(x=dates['Date'], y=dates['Total'])]
    layout = go.Layout(title='Total Registers By Day Since: {0}, To: {1}. For {2}'.format(str(since), str(to), evento))
    figure = go.Figure(data=data, layout=layout)
    return figure
