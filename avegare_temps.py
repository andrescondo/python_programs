#-*- coding: utf-8 -*-


def avegare_temps(temps):
  sum_of_temps = 0

  for temp in temps:
    sum_of_temps += float(temp)

  return sum_of_temps / len(temps)


if __name__ == '__main__':
  temps = [21, 24, 22, 24, 20, 23, 24]

  avegare = avegare_temps(temps)

  print('La temperatura promedio es {}'.format(avegare))