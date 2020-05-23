import pandas as pd


def concat(X, Y, axis = 1, columns= []):
    data = pd.concat([X, Y], axis=axis)
    data.columns = columns
    return data