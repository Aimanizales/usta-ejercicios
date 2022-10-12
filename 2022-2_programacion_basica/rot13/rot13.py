# Algoritmo de cifrado Cesar y/o ROT13

alfabet = 'ABCDEFGHIJKLMNNÑOPQRSTUVWXYZ1234567890 '
alfabetLength = len(alfabet)
indexFactor = 3

def init():
    stringToEncript = input('\n>>>>> Escriba una palabra a transformar: ').upper()

    print(f'1. Original:\t{stringToEncript}')

    encriptedString = ''

    iterator = 0
    while iterator < len(stringToEncript):
        currentLetter = stringToEncript[iterator]
        letterPosInAlfabet = alfabet.find(currentLetter)

        newIndexAlfabet = letterPosInAlfabet + indexFactor

        if newIndexAlfabet > alfabetLength - 1:
            newIndexAlfabet = newIndexAlfabet - alfabetLength
        # print(f'{str(letterPosInAlfabet)}:{newIndexAlfabet}')

        newLetter = alfabet[newIndexAlfabet]

        encriptedString += newLetter
        # print(currentLetter + ':' + newLetter)

        iterator += 1

    print(f'2. Encriptada:\t{encriptedString}')
    init()

init()
