import numpy as np

arr = np.array([[1, 2], [3, 4]])
# Elevado a potencia de e
print(repr(np.exp(arr)))
#Elevado a potencia de 2
print(repr(np.exp2(arr)))
arr2 = np.array([[2,10], [np.e, np.pi]])
# Logaritmo natural
print(repr(np.log(arr2)))
# Logaritmo com base 10
print(repr(np.log10(arr2)))

##### Power
arr = np.array([[1, 2], [3, 4]])
# Eleva 3 à potência de cada número de arr
print(repr(np.power(3, arr)))
arr2 = np.array([[10.2, 4], [3, 5]])
#Eleve arr2 à potência de cada número em arr
print(repr(np.power(arr2, arr)))