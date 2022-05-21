import random

cities = ['Paris', 'Amsterdam', 'Berlin', 'Praga']
ticketsPerCity = {}
ticketsToVienna = []
numTicketSequence = 0
originCity = ''

# 1. Primera función que se ejecuta:
def init():
    initTicketsPerCity()
    selectOption()

# 2. Esta función crea una lista vacía para cada 
# ciudad, de acuerdo a la variable cities:
def initTicketsPerCity():
    for city in cities:
        ticketsPerCity[city] = []

def printTicketList():
    print('\nLISTA DE TICKETS:')
    global ticketsPerCity
    for key, value in ticketsPerCity.items():
        print(f'- {key}:')
        m = 1

        for ticket in value:
            if ticket:
                print(f'  {m}. {ticket}')
                m += 1
            else:
                print('[]')

    print(f'\nLISTA TOTAL DE TICKETS A VIENA ({len(ticketsToVienna)}):')
    n = 1
    for ticket in ticketsToVienna:
        print(f'   {n}. {ticket}')
        n += 1

# Esta función es transversal a la aplicación y solo es para mostrar la
# información actualizada de las ciudades y su número de tickets.
# Muestra las ciudades numeradas para mayor facilidad al momento de
# elegir una, usando el parámetro hideNumbers:
def showCitiesInfo(hideNumbers = False):
    if hideNumbers == True:
        print('\nCANTIDAD DE TICKETS COMPRADOS POR CIUDAD:')
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
def selectCityNumber():
    cityNumberArray = int(input('\n>> Ingrese el número de la ciudad: ')) - 1
    if cityNumberArray >= len(cities) or cityNumberArray < 0:
        print('Seleccione correctamente el número de la ciudad:')
        selectCityNumber()
    else:
        return cityNumberArray

# Inicia el proceso de escoger la ciudad para insertar el nuevo ticket:
def initInsertInfo():
    global originCity
    originCity = input('>> Ciudad de origen del turista: ')

    print('\n¿DESDE QUÉ CIUDAD DESEA INICIAR EL TOUR?:')
    showCitiesInfo()

    cityNumberArray = selectCityNumber()
    cityNameSelected = cities[cityNumberArray]

    print(f'Ciudad desde donde se iniciará el tour: {cityNameSelected}\n')

    ticket = generateTicketInfo(originCity)

    insertTicketIntoCitiesList(ticket, cityNumberArray)

def getMonthDeparture():
    print('Ingrese número del mes de partida (1 a 12):')
    departureMonth = int(input('>> '))

    if departureMonth < 1 or departureMonth > 12:
        print('El número del mes debe ser entre 1 y 12:')
        getMonthDeparture()

    return getDayDeparture(departureMonth)

def getDayDeparture(departureMonth):
    numDaysMonth = 30
    longestMonts = [1,3,5,7,8,10,12]
    if departureMonth in longestMonts:
        numDaysMonth = 31
    elif departureMonth == 2:
        numDaysMonth = 28
    print(f'Ingrese el número del día de partida (1 a {numDaysMonth}):')
    departureDay = int(input('>> '))

    if departureDay < 1 or departureDay > numDaysMonth:
        print(f'El número del día debe ser entre 1 y {numDaysMonth}:')
        getDayDeparture(departureMonth)

    return [departureMonth, departureDay, 2022]

def generateTicketInfo(city):
    global numTicketSequence
    numTicketSequence += 1

    departureDate = getMonthDeparture()

    # Creación del ticket:
    ticket = dict(
        ticket_id = random.randint(0, 100000),
        ref_number = '0' + str(numTicketSequence),
        departure_city = city,
        departure_date = departureDate
    )

    return ticket

# Creado el ticket, se inserta en las ciudades correspondientes:
def insertTicketIntoCitiesList(ticket, cityNumberArray):
    cityNumberCounter = cityNumberArray

    if cityNumberCounter < len(cities):
        currentCityName = cities[cityNumberCounter]
        
        global ticketsPerCity
        ticketsPerCity[currentCityName].append(ticket)

        # Si no se duplica el ticket usando dict(), se edita
        # la referencia del ticket original:
        modifiedTicket = dict(ticket)

        cityNumberCounter += 1
        modifiedTicket["departure_city"] = cities[cityNumberCounter - 1]

        insertTicketIntoCitiesList(modifiedTicket, cityNumberCounter)

    ticketsToVienna.append(ticket)

    printTicketList()
    selectOption()

def deleteViennaTicketFIFO():

    if len(ticketsToVienna) == 0:
        print('\nLa lista de Viena está vacía.')
    else:
        ticketsToVienna.pop(0)
        print(f'\nEliminado primer ticket de la lista de Viena')
    
    selectOption()

# El controlador principal de la aplicación:
def selectOption():
    print('\n'
        '========================================\n'
        '1: Insertar nuevo ticket\n'
        '2: Borrar primer ticket de Viena (FIFO)\n'
        '3: Ver cantidad de tickets comprados por ciudad\n'
        '4: Ver lista completa de tickets\n'
        '5: Salir de la aplicación'
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