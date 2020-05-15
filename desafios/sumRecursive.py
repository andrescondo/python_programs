

def run(num):

    if num == 0:
        return 0

    else: 
        return num + run(num - 1)

        

if __name__ == '__main__':
    print('S U M A - R E C U R S I V A')
    num = int(input('Ingrese un numero entero: '))
    result =  run(num)

    print('El resultado es: {}'.format(result))