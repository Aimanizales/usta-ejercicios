# Calcular la suma por cada fila de una matriz cuadrada, 
# así como la media aritmética. 
# Cada posición de la matriz se genera 
# como numero aleatorio entre 1 hasta 10.

import numpy as np

def createSquareMatrix():
    global A
    global matrixSize

    matrixSize = np.random.randint(2,7)
    A = np.random.randint(1,10, size = (matrixSize, matrixSize))
    print(f"Matriz A de {matrixSize} x {matrixSize}:\n{A}")

def init():
    createSquareMatrix()
    sumarFilasMetodo1()
    sumarFilasMetodo2()

def sumarFilasMetodo1():
    B = np.zeros((matrixSize, 2), dtype = float)
    # print(range(len(A)))
    
    for nRow in range(len(A)):
        row = A[nRow]
        # print(f'row {nRow} = {row}')
        # print(f'nRow {nRow} = {A[nRow, 0]}')
        for n in range(len(A)):
            B[nRow, 0] += A[nRow, n]
            B[nRow, 1] = round(B[nRow, 0] / 3, 2)
            # print(A[nRow, n])
    
    print(
        '\nResultado con método 1 usando for()\n[suma, media]:\n',
        B
    )

def sumarFilasMetodo2():
    print('\nResultado con método 2 usando método iterable sum():')
    
    for nRow in range(len(A)):
        sumRow = sum(A[nRow])
        mediaRow = round(sumRow / len(A), 2)
        print(f'suma = {sumRow} | media = {mediaRow}')

init()