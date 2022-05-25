import numpy as np
from scipy.sparse import csr_matrix

# Create a 2D array (5x5):
arrayA =  np.array([
    [0, 0, 3, 0, 0],
    [0, 5, 2, 0, 0],
    [0, 0, 0, 4, 0],
    [7, 0, 0, 0, 0],
    [0, 0, 0, 1, 8]
])

print(csr_matrix(arrayA))