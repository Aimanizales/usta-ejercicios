import numpy as np
from scipy.sparse import csr_matrix

# Create a 2D array (5x5):
arrayA =  np.array([
    [0, 0, 0, 0, 0],
    [0, 5, 2, 0, 0],
    [0, 0, 0, 0, 0],
    [7, 0, 0, 0, 0],
    [0, 0, 0, 1, 8]
])

IA = csr_matrix(arrayA).indptr
AA = csr_matrix(arrayA).data
JA = csr_matrix(arrayA).indices
AAshape = csr_matrix(arrayA).shape

print('arrayA =\n', arrayA)
# print(csr_matrix(arrayA))
print('AAshape:', AAshape)
print('\nIA:', IA)
print('AA:', AA)
print('JA:', JA)

# Method 1:
arrayB = csr_matrix((AA, JA, IA), shape=AAshape).toarray()
print('\narrayB =\n', arrayB)


#Method 2:
# arrayC = 
i = 0
for m in range(len(IA) - 1):
    if IA[i] == IA[i + 1]:
        print('jueputa', i)
    i += 1

# for n in range(len(IA) - 1):

#    arrayB.append([])
#    arrayB[JA[n]].append(AA[n])
#    n += 1