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

AAshape = csr_matrix(arrayA).shape
IA = csr_matrix(arrayA).indptr
AA = csr_matrix(arrayA).data
JA = csr_matrix(arrayA).indices

print('arrayA =\n', arrayA, '\n\n')
# print(csr_matrix(arrayA))


print('AAshape:', AAshape)
print('IA:', IA)
print('AA:', AA)
print('JA:', JA, '\n\n')

# Método 1 (Reconstrucción de matriz usando scipy.sparse):
arrayB = csr_matrix((AA, JA, IA), shape=AAshape).toarray()
# print('arrayB =\n', arrayB)

#Método 2 (Reconstrucción matriz sin usar scipy.sparse):
# Propuesta algoritmo:
# Iterar sobre IA:
#         R  Dato.   Col
# 0 - 0 = 0  Ceros
# 0 - 2 = 2  [0, 1]. 1, 2
# 2 - 2 = 0  Ceros
# 2 - 3 = 1  [2].    0
# 3 - 5 = 2  [3, 4]. 3, 4
# 5

arrayC = []
sizeNewSquareMatrix = len(IA) - 1
indexIA = 0
indexAA = 0
elementsPerRow = 0
accumulatorAA = 0

for nRow in range(sizeNewSquareMatrix):
    elementsPerRow = IA[indexIA + 1] - IA[indexIA]
    row = []
    for i in range(sizeNewSquareMatrix):
        row.append(0)
    
    if elementsPerRow == 0:
        print(f'\n> fila {indexIA}: solo ceros')

        arrayC.append(row)

    else:
        accumulatorAA += elementsPerRow
        print(f'\n> fila {indexIA}: {elementsPerRow} items')
        # print(f'  accumulatorAA: {accumulatorAA}')
        print(f'  elementos a traer:')
        for item in range(elementsPerRow):
            print(f'  {AA[indexAA]} en la columna {JA[indexAA]}')
            row[JA[indexAA]] = AA[indexAA]
            indexAA += 1
            if indexAA == accumulatorAA:
                continue
        arrayC.append(row)
    print(f'arrayC = {arrayC}')
    indexIA += 1