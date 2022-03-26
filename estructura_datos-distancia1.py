cities = ['Paris', 'Amsterdam', 'Berlin', 'Prague', 'Vienna']
ticketsPerCity = {}
idGenerator = 0000
MAX_UNITS = 20

def init():
    initTicketsPerCity()
    selectOption()

def showCitiesInfo(hideNumbers = False):
    count = 1
    for city in cities:
        numTickets = len(ticketsPerCity[city])
        message = str(numTickets) + ' tickets'
        if numTickets == 1:
            message = str(numTickets) + ' ticket'
        counter = str(count) + '. '
        if hideNumbers:
            counter = ''
        print(f' - {counter}{city} -- [{message}]')
        count += 1

def initInsertInfo():
    print('\n¿A qué ciudad desea insertar el tiquete?:')
    showCitiesInfo()

    selectedCity = selectCity()
    print(f'Ciudad seleccionada: {cities[selectedCity]}\n')
    insertTicketInfo(selectedCity)

def selectCity():
    selectedCity = int(input('\n>> Ingrese el número de la ciudad: ')) - 1
    if selectedCity >= len(cities) or selectedCity < 0:
        print('Seleccione correctamente el número de la ciudad')
        selectCity()
    else:
        return selectedCity

# 
def initTicketsPerCity():
    print(f'Hay {len(cities)} ciudades para este viaje.')
    cityCounter = 0
    for city in cities:
        ticketsPerCity[city]=[]
        cityCounter += 1
    showCitiesInfo(True)

def insertTicketInfo(selectedCity):
    city = input('>> Ingrese la ciudad de origen: ')
    startDate = input('>> Ingrese la fecha de inicio (dd/mm/aaaa): ')

    ticket = dict(ticketId=idGenerator + 1, city=city, startDate=startDate)

    insertTicketIntoCityList(ticket, selectedCity)

def insertTicketIntoCityList(ticket, selectedCity):
    currentCity = cities[selectedCity]
    ticketsPerCity[currentCity].append(ticket)
    print(f'Ticket ingresado a la ciudad de {currentCity}\n')
    print(ticketsPerCity)
    selectOption()

def initDeleteTicket():
    print('\n¿A qué ciudad desea eliminar tiquete?:')
    showCitiesInfo()

    selectedCity = selectCity()
    print(f'Ciudad seleccionada: {cities[selectedCity]}\n')
    deleteTicketInfo(selectedCity)

def deleteTicketInfo(selectedCity):
    if len(ticketsPerCity[selectedCity]) > 0:
        print(f'\nSe borrará el último ticket ingresado a la ciudad de {cities[selectedCity]}')
    else:
        print(f'{cities[selectedCity]} no posee tickets ingresados aún.')
        selectOption()

def selectOption():
    print('\nSeleccione una de las opciones:')
    print('  1. Insertar un ticket')
    print('  2. Borrar un ticket')
    selectedOption = int(input('\n>> Ingrese una opción: '))
    if selectedOption < 1 or selectedOption > 2:
        print('Seleccione correctamente una opción')
        selectOption()
    elif selectedOption == 1:
        initInsertInfo()
    elif selectedOption == 2:
        initDeleteTicket()

init()