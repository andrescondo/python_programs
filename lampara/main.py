#-*- coding: utf-8 -*-

def run():
    lamp = Lamp(_is_turned_on= False)

    while True:
        command = str(raw_input('''
            Que deseas hacer?

            [p]render
            [a]pagar
            [s]alir
            ''')).lower()

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break

if __name__ == '__main__':
        run()
