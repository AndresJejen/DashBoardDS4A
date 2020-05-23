from sklearn.linear_model import LinearRegression


def LinearRegressionModel(X, y):
    """
    Genera una regresión lineal ingresando los parámetros
    :param X:
    :param y:
    :return:
    """
    X, y = X.values.reshape(-1, 1), y.values.reshape(-1, 1)
    reg = LinearRegression(fit_intercept=False).fit(X, y)
    return reg.score(X, y), reg.coef_, reg.intercept_
