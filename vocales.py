# 1. Almacenar vocales en lista:
vocales = ['a', 'e', 'i', 'o', 'u']

print(f'vocales = {vocales}')

# 2. Eliminar de la lista las vocales en posiciones impares (contanto la primera posición como cero)
vocalesImpares = []

for vocal in vocales:
    # 2. se trae la posición de cada vocal (la primera posición es cero):
    posVocal = vocales.index(vocal)

    print(vocal, posVocal, posVocal % 2)

    #3. Se evalúa si la posición es módulo dos (así se sabe si la posición es impar o es par):
    if posVocal % 2 == 0:
        # 4. Si es par, agrega la vocal a la matriz vocalesImpares:
        vocalesImpares.append(vocal)

# 5. Se imprime la matriz resultante:
print(vocalesImpares)