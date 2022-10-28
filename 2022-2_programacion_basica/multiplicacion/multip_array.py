# Tareas:
# 1. Definir tamaño de matriz cuadrada (n)
# 2. Generar matriz A
# 3. Generar matriz B
# 4. Multiplicar
# 5. Mostrar resultado

import numpy as np

np.random.seed()

def multiply_matrix(A, B):
    global C

    if  A.shape[1] == B.shape[0]:
        shapeNewMatrix = (A.shape[0], B.shape[1])
        C = np.zeros(shapeNewMatrix, dtype = int)

        # iterar sobre filas de A:
        for row in range(len(A)):
            # iterar sobre columnas de B:
            for col in range(len(B[0])):
                for elt in range(len(B)):
                    C[row, col] += A[row, elt] * B[elt, col]
        return C
    else:
        return "No se pueden multiplicar A y B."

def init():
    matrixSize = np.random.randint(1,10)
    print(matrixSize)
    print(f'Multiplicación de matriz de {matrixSize} x {matrixSize}:')
    A = np.random.randint(1,10, size = (matrixSize, matrixSize))
    B = np.random.randint(1,10, size = (matrixSize, matrixSize))

    print(f"Matriz A:\n {A}\n")
    print(f"Matriz B:\n {B}\n")

    print(f'======== Matriz resultante C de {matrixSize} x {matrixSize}: ==========')
    print(multiply_matrix(A, B))

init()