# 
print('\nRealice un ciclo donde si el numero es excatamente divisible para 3 elevalo al cuadrado, y si el numero es 22 cierra el ciclo\n')
for i in range(30):
  if i % 3 == 0:
    print(i ** 2)
  elif i == 22:
    break

print('\n\n')


for a in range(30):
  if a % 3 == 0:
    print(a)
  elif a == 22:
    break