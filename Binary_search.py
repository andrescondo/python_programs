# -*- coding: utf-8 -*-

def binary_search(numbers, number_to_find, low, high):
  if low > high:
    return False

  mid = (low + high) / 2

  if numbers[mid] == number_to_find:
    return True

  elif numbers[mid] > number_to_find:
    return binary_search(numbers, number_to_find, low, mid - 1)
  else:
    return binary_search(numbers, number_to_find, mid + 1 , high)


if __name__ == '__main__':

  numbers = [2,5,7,3,5,9,7,4,45,12,78,89,12,54,56,1,47,97,32,30]
  # Formas de ordenar listas desordenadas
  #numbers.sort() # Forma 1
  numbers = sorted(numbers) # Forma 2
  #----------------------------------------

  number_to_find = int(raw_input('Ingrese un numero: '))

  result = binary_search(numbers, number_to_find, 0 , len(numbers) - 1)


  if result is True:
    print('El numero si esta en la lista.')
  else:
    print('El numero NO esta en la lista.')
