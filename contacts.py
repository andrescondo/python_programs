

def run():

    while True:
        command = str(raw_input('''
            Que deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contacto
            [s]alir

            '''))

        if command == 'a':
            print('añadir contacto')

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
    run()
