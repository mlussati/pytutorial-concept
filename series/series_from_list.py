import pandas as pd

list_valores = range(1, 6)
index = ["a", "b", "c", "d", "e"]
series = pd.Series(list_valores, index)
print(series)

valor_acesso = "d"
print("Index {} -> valor {}".format(valor_acesso, series[valor_acesso]))