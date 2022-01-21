import numpy as np

arr = np.array([np.nan, 1, 2])
print(repr(arr))

arr = np.array([np.nan, 'abc'])
print(repr(arr))

# A linha a abaixo pode resultar em Value Erro:
# Se vc descomentar a linha 11 e rodar
# np.array([np.nan, 1, 2], dtype=np.int32)
np.array([np.nan, 1, 2], dtype=np.float32)