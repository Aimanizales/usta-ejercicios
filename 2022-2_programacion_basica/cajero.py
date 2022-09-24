import random

bankNotesQuantities = {
    10000: 100,
    20000: 50,
    50000: 20,
    100000: 10
}

def printSelectedValue(amount):
    valueWithDecimals = '{0:,}'.format(amount)
    print(
        '------------------------------------\n'
        f'Valor digitado: ${valueWithDecimals}\n'
        '------------------------------------\n'
    )

def calculateBankNotesToWithdraw(amount):
    bankNotesQuantities[10000] -= 1
    print(bankNotesQuantities[10000])
    selectOption()

def calculateSavings():
    # saldo: mayor a 100,000 y menor a 300,000.
    print('\n'
        '========================================\n'
        f'Su saldo es de ${100000 + random.randint(1, 20) * 10000}\n'
        'Gracias.'
    )

def selectOption():
    valueToWidtraw = input('\n>>>>> Digite el monto a retirar (mínimo $10,000, máximo: $600,000):')
    if valueToWidtraw.isdigit():
        valueToWidtraw = int(valueToWidtraw)
        printSelectedValue(valueToWidtraw)
        if valueToWidtraw < 10000:
            print('El monto debe ser igual o mayor a $10,000')
            selectOption()
        if valueToWidtraw > 600000:
            print('El monto debe ser igual o menor a $600,000')
            selectOption()
        if valueToWidtraw % 10000 != 0:
            print('El valor debe ser en unidades de 10,000')
            selectOption()
        else:
            calculateBankNotesToWithdraw(valueToWidtraw)
            # quit()
    else:
        print('Debe digitar solo números.')
        selectOption()

# 1. Primera función que se ejecuta:
def init():
    selectOption()

init()