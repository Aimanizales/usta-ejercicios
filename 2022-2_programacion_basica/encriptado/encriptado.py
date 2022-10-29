# Algoritmo de cifrado

alfabet = 'ABCDEFGHIJKLMNNÑOPQRSTUVWXYZ1234567890 '
alfabetLength = len(alfabet)

def init():
    global indexFactor
    stringToEncript = input('\n>>>>> Escriba una palabra a transformar: ').upper()
    indexFactor = int(input('\n>>>>> Digite un número (posiciones que se moverán las letras): '))

    print(f'\nFrase original: {stringToEncript}')
    print(f'Factor de desplazamiento: {indexFactor}')

    encriptedString = ''

    iterator = 0
    while iterator < len(stringToEncript):
        currentLetter = stringToEncript[iterator]
        letterPosInAlfabet = alfabet.find(currentLetter)

        newIndexAlfabet = letterPosInAlfabet + indexFactor

        if newIndexAlfabet > alfabetLength - 1:
            newIndexAlfabet = newIndexAlfabet - alfabetLength

        newLetter = alfabet[newIndexAlfabet]

        encriptedString += newLetter

        iterator += 1

    print(f'Frase encriptada: {encriptedString}')
    init()

init()
