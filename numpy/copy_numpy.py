import numpy as np

a = np.array([0, 1])
b = np.array([9, 8])
c = a
print('Array a: {}'.format(repr(a)))
c[0]= 5
print('Array a: {}'.format(repr(a)))

d = b.copy()
d[0] = 6
print('Array d: {}'.format(repr(d)))
