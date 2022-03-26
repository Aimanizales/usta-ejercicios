import random

cities = ['Paris', 'Amsterdam', 'Berlin', 'Prague', 'Vienna']
ticketsPerCity = {}
MAX_UNITS_PER_CITY = 20
numTicketSequence = 0

# 1. Primera función que se ejecuta:
def init():
    initTicketsPerCity()
    selectOption()

# 2. Esta función crea una lista vacía para cada 
# ciudad de acuerdo a la variable cities:
def initTicketsPerCity():
    print(f'Hay {len(cities)} ciudades para este viaje.')
    print(f'Cada ciudad puede tener hasta {MAX_UNITS_PER_CITY} tickets.')
    cityCounter = 0
    for city in cities:
        ticketsPerCity[city]=[]
        cityCounter += 1
    showCitiesInfo(True)

# Esta función es transversal a la aplicación y solo es para mostrar la
# información actualizada de las ciudades y su número de tickets.
# Muestra las ciudades numeradas para mayor facilidad al momento de elegir
# una usando el parámetro hideNumbers:
def showCitiesInfo(hideNumbers = False):
    if hideNumbers == True:
        print('\nCIUDADES:')
    count = 1
    for city in cities:
        numTickets = len(ticketsPerCity[city])
        message = str(numTickets) + ' tickets'
        if numTickets == 1:
            message = str(numTickets) + ' ticket'
        counter = str(count) + '. '
        if hideNumbers:
            counter = ''
        print(f' - {counter}{city} [{message}]')
        count += 1

# Permite únicamente seleccionar la ciudad digitando un número:
def selectCity():
    selectedCity = int(input('\n>> Ingrese el número de la ciudad: ')) - 1
    if selectedCity >= len(cities) or selectedCity < 0:
        print('Seleccione correctamente el número de la ciudad')
        selectCity()
    else:
        return selectedCity

# Inicia el proceso de escoger la ciudad para insertar el nuevo ticket:
def initInsertInfo():
    print('\n¿A qué ciudad desea insertar el tiquete?:')
    showCitiesInfo()

    selectedCity = selectCity()
    print(f'Ciudad seleccionada: {cities[selectedCity]}\n')
    insertTicketInfo(selectedCity)


def insertTicketInfo(selectedCity):
    global numTicketSequence
    numTicketSequence += 1
    print(f'Ingrese información del ticket:')

    # Datos del ticket ingresados por el usuario:
    city = input('>> Ciudad de origen: ')
    startDate = input('>> Fecha de inicio (dd/mm/aaaa): ')

    # Creación del ticket:
    ticket = dict(
        ticketId = random.randint(0, 100000),
        reference = numTicketSequence,
        city = city,
        startDate=startDate
    )

    insertTicketIntoCityList(ticket, selectedCity)

    numTicketSequence += 1

# Después de creado el ticket, se inserta en la ciudad correspondiente:
def insertTicketIntoCityList(ticket, selectedCity):
    currentCity = cities[selectedCity]
    ticketsPerCity[currentCity].append(ticket)
    print(f'Ingresado ticket para {currentCity}!!!\n')
    print(ticketsPerCity)
    selectOption()

# Selecciona la ciudad a borrar el ticket:
def initDeleteTicket():
    print('\n¿A qué ciudad desea eliminar tiquete?:')
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
    print('\n1: Insertar ticket')
    print('2: Borrar ticket')
    print('3: Ver lista de tickets')
    print('4: Salir de la aplicación')
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