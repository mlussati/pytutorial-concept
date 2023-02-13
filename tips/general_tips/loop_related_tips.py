# Avoid range() in loops
seq1=[1,2,3,4]
seq2=[5,6,7,8]
# for i in range(len(seq)):
#     print(seq[i])

# print(' ')

# for item in seq:
#     print(item)

# Naturalmente, podemos usar o indice para qualquer outra finalidade, 
# por exemplo, para processar apenas itens impares
# for i, item in enumerate(seq):
#     #print(i, item)
#     if i%2:
#         print(i)

# for item1,item2 in zip(seq1,seq2):
#     print(item1, item2)

# for items in zip(seq1,seq2):
#     print(*items)

# seqs=[seq1,seq2]
# for items in zip(*seqs):
#     print(*items)

# Avoid comprehension expressions, if needed
def square(x):
    return x*x

# [print(square(x)) for x in range(4)]

##############################################
evenSquares=[square(x) for x in range(1, 10) if x%2==0]
oddSquares=[square(x) for x in range(1, 10) if not x%2==0]
print(evenSquares)
print(oddSquares)