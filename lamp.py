
class Lamp:

    _LAMP = ['''
              .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|

    ''']

    def __init__(self, _is_turned_on):
        self._is_turned_on = _is_turned_on

    def turn_on(self):
        self._is_turned_on = True
        self._display_image()


    def turn_off(self):
        self._is_turned_on = False
        self._display_image()



    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMP[0])
        else:
            print(self._LAMP[1])


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
