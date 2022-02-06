import pandas as pd

dicionario = {"a": 1, "b": 14, "c": 24}

series = pd.Series(dicionario)
print(series)
idx = "b"
print("meu index {} -> valor {}".format(idx, series[idx]))