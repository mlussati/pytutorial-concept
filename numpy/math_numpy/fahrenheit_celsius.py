import numpy as np

def fahrenheith2c(temperatura):
    return (5/9) * (temperatura-32)

fahrenheits = np.array([34, -5, 16, -42])
celsius = fahrenheith2c(fahrenheits)
print('Celsius: {}'.format(repr(celsius)))