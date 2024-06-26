# -*- coding: utf-8  -*-

def first_not_repeating_char(char_sequence):
    seen_letters = {}

    for idx , letter in enumerate(char_sequence):
        if letter not in seen_letters:
            seen_letters[letter] = ( idx, 1)
        else:
            seen_letters[letter] = (seen_letters[letter] [0], seen_letters[letter] [1] + 1)

    final_letters = []
    for key, value in seen_letters.iteritems():
        if value[1] == 1:
            final_letters.append( (key, value))

    not_reapeat_letters = sorted(final_letters, key =lambda value : value[1])

    if not_reapeat_letters:
        return not_reapeat_letters[0] [0]
    else:
        return '_'



if __name__ == '__main__':
    char_sequence = str(raw_input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if  result == '_':
        print('Todos los caracteres se repiten. ')
    else:
        print('El primer caracter no respetido es: {}'.format(result))
