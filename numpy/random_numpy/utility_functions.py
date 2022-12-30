import numpy as np

np.random.seed(1)
print(np.random.randint(10))
random_arr = np.random.randint(3, high=100, size=(2, 2))
print(repr(random_arr))

### Shuffle

vec = np.array([1, 2, 3, 4, 5])
np.random.shuffle(vec)
print(f"This is shuffle {repr(vec)}")
np.random.shuffle(vec)
print(f"This is shuffle {repr(vec)}")

matrix = np.array([ [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
np.random.shuffle(matrix)
print(repr(matrix))