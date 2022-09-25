import random

bankNotes = [
    {
        'value': 100000,
        'quantity': 10,
    },
    {
        'value': 50000,
        'quantity': 20,
    },
    {
        'value': 20000,
        'quantity': 50,
    },
    {
        'value': 10000,
        'quantity': 100,
    },
]

def formatNumber(number):
    return '{0:,}'.format(number)

def printSelectedValue(amount):
    print(
        '\n----------------------------------------\n'
        f'Valor digitado: ${formatNumber(amount)}\n'
        '----------------------------------------\n'
    )

def calculateBankNotesToWithdraw(amount):
    iterator = 0
    accumulator = 0
    bankNotesToDeliver = [0,0,0,0]

    while accumulator < amount:
        accumulator += bankNotes[iterator]['value']
        bankNotesToDeliver[iterator] += 1
        bankNotes[iterator]['quantity'] -= 1
        # print(f'Se sumó un billete de {bankNotes[iterator]["value"]}')
        # print(f'accumulator = {accumulator}')
        
        if accumulator == amount:
            # print(f'Se logró el monto de {accumulator}')
            break

        if accumulator > amount:
            accumulator -= bankNotes[iterator]['value']
            bankNotesToDeliver[iterator] -= 1
            bankNotes[iterator]['quantity'] += 1

            # print(f'Se restó {bankNotes[iterator]["value"]} porque se pasa')
            # print(f'accumulator = {accumulator}')
        
        iterator += 1
        if iterator > 3:
            iterator = 0
    
    resumeBankNotes(bankNotesToDeliver)

def resumeBankNotes(bankNotesToDeliver):
    n = 0
    print('======================= El cajero entrega ========================')
    for numOfBankNotes in bankNotesToDeliver:
        currentBankNote = bankNotes[n]["value"]
        valuePerBankNote = currentBankNote * numOfBankNotes

        currentBankNoteWithFormat = formatNumber(currentBankNote)
        valuePerBankNoteWithFormat = formatNumber(valuePerBankNote)

        billetes = 'billetes'
        if numOfBankNotes == 1:
            billetes = 'billete'

        tabulador = '\t'
        if numOfBankNotes == 0:
            tabulador = '\t\t'

        
        print(
            f'{numOfBankNotes} {billetes} de ${currentBankNoteWithFormat}\t = ${valuePerBankNoteWithFormat}'
            f'{tabulador}Quedan {bankNotes[n]["quantity"]} billetes'
        )
        n += 1
    print('==================================================================')

def calculateSavings():
    # saldo: mayor a 100,000 y menor a 300,000.
    savings = 100000 + random.randint(1, 20) * 10000
    print(
        '\n-----------------------------\n'
        f'Su saldo es de ${formatNumber(savings)}.\n'
        'Gracias.\n'
        '-----------------------------'
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
            calculateSavings()
            quit()
    else:
        print('Debe digitar solo números.')
        selectOption()

# 1. Primera función que se ejecuta:
def init():
    selectOption()

init()