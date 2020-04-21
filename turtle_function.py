# -*- coding: utf-8 -*-

import turtle

def main():
  window = turtle.Screen()
  figure = turtle.Turtle()

  make_figure(figure)

def make_figure(figure):
  side = int(raw_input('Lados de la figura: '))
  length = int(raw_input('Tamaño de los lados: '))


  for i in range(side):
    make_line_and_turn(figure, length)


def make_line_and_turn(figure, length): 
  figure.forward(length)
  figure.left(90)


if __name__ == '__main__':
  main()

turtle.mainloop()