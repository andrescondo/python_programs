# -*- coding: utf-8 -*-

countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}


while True:
    country = str(raw_input('\nEscribe el nombre de un pais: ')).lower()

    try:
        print('La poblacion de {} es: {} millones'.format(country, countries[country]))
    except KeyError:
        print('No tenemos el dato de la poblacion de {}'.format(country))
