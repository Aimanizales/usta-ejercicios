import random

def calculateSavings():
    # saldo: mayor a 100,000 y menor a 300,000.
    print('\n'
        '========================================\n'
        f'Su saldo es de ${100000 + random.randint(1, 20) * 10000}\n'
        'Gracias.'
    )

def selectOption():
    calculateSavings()
    valueToWidtraw = input('\n>>>>> Digite el monto a retirar (mínimo $10,000):')
    if valueToWidtraw.isdigit():
        valueToWidtraw = int(valueToWidtraw)
        if valueToWidtraw < 10000:
            print('El monto debe ser igual o mayor a $10,000')
            selectOption()
        if valueToWidtraw % 10000 != 0:
            print('El valor debe ser en unidades de 10,000')
            selectOption()
        else:
            calculateSavings()
            quit()
    else:
        print('Debe digitar solo números.')
        selectOption()

# 1. Primera función que se ejecuta:
def init():
    selectOption()

init()