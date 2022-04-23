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
    showCitiesInfo(True)

def printTicketList():
    print('Tickets por ciudad de origen:')
    for key, value in ticketsPerCity.items():
        print(f'- {key}:')
        m = 1
        for ticket in value:
            if ticket:
                print(f' {m}. {ticket}')
                m += 1
            else:
                print('[]')

    print(f'\nTickets a Viena ({len(ticketsToVienna)}):')
    n = 1
    for ticket in ticketsToVienna:
        print(f' {n}. {ticket}')
        n += 1

# Esta función es transversal a la aplicación y solo es para mostrar la
# información actualizada de las ciudades y su número de tickets.
# Muestra las ciudades numeradas para mayor facilidad al momento de elegir
# una usando el parámetro hideNumbers:
def showCitiesInfo(hideNumbers = False):
    if hideNumbers == True:
        print('\nCantidad de tickets por ciudad de origen:')
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
        print(f' - {counter}{city} {message}')
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
    print('\nDigite el número de la ciudad de origen:')
    showCitiesInfo()

    selectedCity = selectCity()
    cityNameSelected = cities[selectedCity]

    print(f'Ciudad seleccionada: {cityNameSelected}\n')
    insertTicketInfo(selectedCity)


def insertTicketInfo(selectedCity):
    global numTicketSequence
    numTicketSequence += 1
    print(f'Ingrese fecha de partida (dd/mm/aaaa):')

    # Datos del ticket ingresados por el usuario:
    departureDate = input('>> ')

    # Creación del ticket:
    ticket = dict(
        ticket_id = random.randint(0, 100000),
        reference_number = numTicketSequence,
        origin_city = cities[selectedCity],
        departure_date = departureDate
    )

    insertTicketIntoCityList(ticket, selectedCity)

    numTicketSequence += 1

# Después de creado el ticket, se inserta en la ciudad correspondiente:
def insertTicketIntoCityList(ticket, selectedCity):
    currentCity = cities[selectedCity]
    ticketsPerCity[currentCity].append(ticket)
    ticketsToVienna.append(ticket)

    print(f'\nTicket ingresado para {currentCity}!!!\n')

    printTicketList()
    selectOption()

# Selecciona la ciudad a borrar el ticket:
def initDeleteTicket():
    print('\nDigite el número de la ciudad de origen:')
    showCitiesInfo()

    selectedCity = selectCity()
    print(f'\nCiudad seleccionada: {cities[selectedCity]}\n')
    deleteTicketInfo(selectedCity)

# Borra el ticket de la ciudad elegida. Valida si la ciudad no tiene: 
def deleteTicketInfo(selectedCity):
    currentCity = cities[selectedCity]
    currentCityTickets = ticketsPerCity[currentCity]

    if len(currentCityTickets) == 0:
        print(f'\n{cities[selectedCity]} no posee tickets ingresados aún.')
    else:
        currentCityTickets.pop()
        print(f'\nEliminado último ticket de {cities[selectedCity]}')
        showCitiesInfo(True)
    
    selectOption()

# El controlador principal de la aplicación:
def selectOption():
    print('\n'
        '1: Insertar\n'
        '2: Borrar\n'
        '3: Mostrar lista\n'
        '4: Salir'
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
            initDeleteTicket()
        elif selectedOption == 3:
            showCitiesInfo(True)
            selectOption()
        else:
            quit()
    else:
        print('La opción debe ser un número.')
        selectOption()

init()