import numpy as np

print(np.random.randint(5))
print(np.random.randint(5))
print(np.random.randint(4, high=10))

random_arr = np.random.randint(-3, high=14,
                                size=(2, 2))

print(repr(random_arr))