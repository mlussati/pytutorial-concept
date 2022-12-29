import numpy as np

arr = np.arange(8)

reshaped_arr = np.reshape(arr, (2, 4))
print(repr(reshaped_arr))
print('Novo shape: {}'.format(reshaped_arr.shape))

reshaped_arr = np.reshape(arr, (-1, 2, 2))
print(repr(reshaped_arr))
print('Novo shape: {}'.format(reshaped_arr.shape))
