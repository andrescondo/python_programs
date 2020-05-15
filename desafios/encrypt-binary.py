#usando python 2.7.18
# -*- coding: utf-8  -*-

KEYS = {
  'a': '97',
  'b': '98',
  'c': '99',
  'd': '100',
  'e': '101',
  'f': '102',
  'g': '103',
  'h': '104',
  'i': '105',
  'j': '106',
  'k': '107',
  'l': '108',
  'm': '109',
  'n': '110',
  'o': '111',
  'p': '112',
  'q': '113',
  'r': '114',
  's': '115',
  't': '116',
  'u': '117',
  'v': '118',
  'w': '119',
  'x': '120',
  'y': '121',
  'z': '122',
  'A': '65',
  'B': '66',
  'C': '67',
  'D': '68',
  'E': '69',
  'F': '70',
  'G': '71',
  'H': '72',
  'I': '73',
  'J': '74',
  'K': '75',
  'L': '76',
  'M': '77',
  'N': '78',
  'O': '79',
  'P': '80',
  'Q': '81',
  'R': '82',
  'S': '83',
  'T': '84',
  'U': '85',
  'V': '86',
  'W': '87',
  'X': '88',
  'Y': '89',
  'Z': '90',
  '0': '48',
  '1': '49',
  '2': '50',
  '3': '51',
  '4': '52',
  '5': '53',
  '6': '54',
  '7': '55',
  '8': '56',
  '9': '57',
  '.': '46',
  ',': '44',
  '?': '63',
  '!': '33',

}


def binary_encrypt(code_ascii):
    encrypt = []
    # print(code_ascii)

    for i in range(len(code_ascii)):
        encrypt = encrypt + [int(code_ascii[i])]
        print(encrypt[i])

        for a in i: 
            binary = encrypt[i] % 2
            print(binary)


        # if encrypt[i] == 0 :
        #     return 0
        # else:



def encrypt(message):
    words = message.split(' ')
    cypher_message = []
    code_ascii = []

    for word in words:
        cypher_words = ''
        for letter in word:
            cypher_words += KEYS[letter]
            code_ascii.append(KEYS[letter])
        
        binary_encrypt(code_ascii)
        

        # cypher_message.append(cypher_words)

    # return ' '.join(cypher_message)






def run():
    command = str(raw_input('''
        C O N V E R T I R - A - B I N A R I O

        [C]IFRAR
        ''')).lower()

    
    if command == 'c':
        message = str(raw_input('Ingrese su mensaje: '))
        cypher_message = encrypt(message)
        print(cypher_message)

       

if __name__ == '__main__':
    run()
