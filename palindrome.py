#-*- coding: utf-8 -*-

def Palindrome(word):
  reversed_letters = []

  for letter in word:
    reversed_letters.insert(0, letter)

  reversed_word = ''.join(reversed_letters)

  if reversed_word == word:
    return True

  return False


if __name__ == '__main__':
  word = str(raw_input('Escriba una palabra: '))
  result = Palindrome(word)

  if result is True:
    print('{} SÍ es un palíndromo '. format(word))
  else:
    print('{} NO es un palíndromo '. format(word))
