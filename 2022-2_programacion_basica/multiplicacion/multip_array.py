# 1. Definir tamaño de matriz cuadrada (n)
# 2. Generar matriz 1
# 3. Generar matriz 2
# 4. Multiplicar
# 5. Mostrar resultado

# import random

# https://geekflare.com/multiply-matrices-in-python/

import numpy as np

np.random.seed(27)
A = np.random.randint(1,10, size = (3,3))
B = np.random.randint(1,10, size = (3,2))
print(f"Matrix A:\n {A}\n")
print(f"Matrix B:\n {B}\n")

def multiply_matrix(A, B):
    global C
    if  A.shape[1] == B.shape[0]:
        C = np.zeros((A.shape[0],B.shape[1]),dtype = int)
        for row in range(rows): 
            for col in range(cols):
                for elt in range(len(B)):
                    C[row, col] += A[row, elt] * B[elt, col]
        return C
    else:
        return "Sorry, cannot multiply A and B."

multiply_matrix(A, B)
# def getRandomNumber(max):
#     print('n', random.randint(1, max))

# def printMatrix():
#     print()

# def init():
#     # print('Multiplicación de matriz')
#     getRandomNumber(10)

# init()