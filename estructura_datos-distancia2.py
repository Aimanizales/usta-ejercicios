import random

cities = ['Paris', 'Amsterdam', 'Berlin', 'Prague']
ticketsPerCity = {}
ticketsToVienna = []
numTicketSequence = 0

# 1. Primera función que se ejecuta:
def init():
    initTicketsPerCity()
    selectOption()

# 2. Esta función crea una lista vacía para cada 
# ciudad de acuerdo a la variable cities:
def initTicketsPerCity():
    for city in cities:
        ticketsPerCity[city] = []

def printTicketList():
    print('\nLISTA DE TICKETS COMPRADOS POR CIUDAD DE INICIO:')
    for key, value in ticketsPerCity.items():
        print(f'- {key}:')
        m = 1
        for ticket in value:
            if ticket:
                print(f'  {m}. {ticket}')
                m += 1
            else:
                print('[]')

    print(f'\nLISTA TOTAL DE TICKETS A VIENNA ({len(ticketsToVienna)}):')
    n = 1
    for ticket in ticketsToVienna:
        print(f'   {n}. {ticket}')
        n += 1

# Esta función es transversal a la aplicación y solo es para mostrar la
# información actualizada de las ciudades y su número de tickets.
# Muestra las ciudades numeradas para mayor facilidad al momento de elegir
# una usando el parámetro hideNumbers:
def showCitiesInfo(hideNumbers = False):
    if hideNumbers == True:
        print('\nCANTIDAD DE TICKETS COMPRADOS POR CIUDAD DE INICIO:')
    count = 1
    message = ''
    for city in cities:
        counter = str(count) + '. '
        if hideNumbers:
            numTickets = len(ticketsPerCity[city])
            message = '\t' + str(numTickets) + ' ticket'
            if numTickets != 1:
                message += 's'
            counter = ''
        print(f' {counter}{city}: {message}')
        count += 1

# Permite únicamente seleccionar la ciudad digitando un número:
def selectCity():
    selectedCity = int(input('\n>> Ingrese el número de la ciudad: ')) - 1
    if selectedCity >= len(cities) or selectedCity < 0:
        print('Seleccione correctamente el número de la ciudad:')
        selectCity()
    else:
        return selectedCity

# Inicia el proceso de escoger la ciudad para insertar el nuevo ticket:
def initInsertInfo():
    print('\n¿DESDE QUÉ CIUDAD DESEA INICIAR EL TOUR?:')
    showCitiesInfo()

    selectedCity = selectCity()
    cityNameSelected = cities[selectedCity]

    print(f'Ciudad seleccionada: {cityNameSelected}\n')
    insertTicketInfo(selectedCity)

def insertTicketInfo(selectedCity):
    global numTicketSequence
    numTicketSequence += 1
    print(f'Ingrese día y mes de partida (dd/mm):')

    # Datos del ticket ingresados por el usuario:
    departureDate = input('>> ')
    originCity = input('>> Ciudad de origen: ')

    # Creación del ticket:
    ticket = dict(
        ticket_id = random.randint(0, 100000),
        ref_number = '000' + str(numTicketSequence),
        origin_city = originCity,
        departure_date = departureDate + '/2022'
    )

    insertTicketIntoCityList(ticket, selectedCity)

    numTicketSequence += 1

# Después de creado el ticket, se inserta en la ciudad correspondiente:
def insertTicketIntoCityList(ticket, selectedCity):
    currentCityNumber = selectedCity
    currentCity = cities[currentCityNumber]
    ticketsPerCity[currentCity].append(ticket)
    if currentCityNumber < len(cities) - 1:
        insertTicketIntoCityList(ticket, currentCityNumber + 1)

    ticketsToVienna.append(ticket)

    print(f'\nTICKET INGRESADO.\n')

    printTicketList()
    selectOption()

def deleteViennaTicketFIFO():

    if len(ticketsToVienna) == 0:
        print('\nLa lista Viena está vacía.')
    else:
        ticketsToVienna.pop(0)
        print(f'\nEliminado primer ticket de la lista Viena')
    
    selectOption()

# El controlador principal de la aplicación:
def selectOption():
    print('\n'
        '========================================\n'
        '1: Insertar ticket\n'
        '2: Borrar primer ticket de Viena (FIFO)\n'
        '3: Ver cantidad de tickets comprados por ciudad\n'
        '4: Ver lista completa de tickets\n'
        '5: Salir'
    )
    selectedOption = input('\n>>>>> Ingrese una opción: ')
    if selectedOption.isdigit():
        selectedOption = int(selectedOption)
        if selectedOption < 1 or selectedOption > 5:
            print('Seleccione correctamente una opción.')
            selectOption()
        elif selectedOption == 1:
            initInsertInfo()
        elif selectedOption == 2:
            deleteViennaTicketFIFO()
        elif selectedOption == 3:
            showCitiesInfo(True)
            selectOption()
        elif selectedOption == 4:
            printTicketList()
            selectOption()
        else:
            quit()
    else:
        print('La opción debe ser un número.')
        selectOption()

init()