

class Contact:

    #constructor (parametros(self, ))
    def __init__(self, name, phone, email ):
        #guion bajo sig. es privada
        self._name = name
        self._phone = phone
        self._email = email


class ContactBook:

    def __init__(self):
        self._contacts = []


    def add(self, name, phone, email):
        print('name: {}, phone: {}, email: {}'.format(name, phone, email))



def run():

    contact_book = ContactBook()

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contacto
            [s]alir

            '''))

        if command == 'a':

            name = str(input('Escriba el nombre del contacto: '))
            phone = str(input('Escribe el tel del contacto: '))
            email = str(input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)

        elif command == 'ac':
            print('actualizar contacto')

        elif command == 'b':
            print('buscar contacto')

        elif command == 'e':
            print('eliminar contacto')

        elif command == 'l':
            print('listar conctactos')

        elif command == 's':
            break
        else:
            print('comando no encontrado')



if __name__ == '__main__':
    print('A G E N D A - D E - C O N T A C T O S ')
    run()
