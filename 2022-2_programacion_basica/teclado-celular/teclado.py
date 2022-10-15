LETTERSPERKEY = [
    ' ',                 #   0
    'ABC', 'DEF', 'GHI', # 1 2 3
    'JKL', 'MNÑ', 'OPQ', # 4 5 6
    'RST', 'UVW', 'XYZ'  # 7 8 9
]

def convertSentenceToNumbers(sentence):
    finalResult = ''
    for letter in sentence:
        finalResult += getKeyNumber(letter)
    print(finalResult)

def getKeyNumber(letter):
    for numberKey, letters in enumerate(LETTERSPERKEY):
        nKey = letters.find(letter)
        if nKey != -1:
            result = ''
            timesToPressKey = nKey + 1
            # print('[012]:', nKey)
            print(f'{letter}: Tecla {numberKey} - {timesToPressKey} veces')
            n = 1
            for n in range(timesToPressKey):
                result += str(numberKey)
                n += 1
    return result

def init():
    sentenceToConvert = input('\n>>>>> Palabra a convertir a teclas numéricas: ').upper()
    print(
        '\n-----------------------------\n'
        f'{sentenceToConvert}\n'
        '-----------------------------'
    )
    convertSentenceToNumbers(sentenceToConvert)

init()