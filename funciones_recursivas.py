print('*** Funciones Recursivas ***')

def funciones_recursivas(numero:int):
    """ Imprime numero, pero de manera recursiva
    :param numero: numeros a imprimir
    """

    if numero == 1:
        print(numero, end=' ')
    else:
        funciones_recursivas(numero - 1,)
        print(numero, end=' ')

# Llamado de la funcion
# funciones_recursivas(5)

def factorial_de_un_numero(numero:int):
    """
    Imprime el factorial del numero ingresado de manera recursiva
    :param numero: numeros a imprimir

    Caso base -> 0! = 1
     - Factorial 0 : = 1
     - Factorial 1 : = 1 * 0! -> 1*1 = 1
     - Factorial 2 : = 2 * 1! -> 2*1 = 2
     - Factorial 3 : = 3 * 2! -> 3*2 = 6
     - Factorial 4 : = 4 * 3! -> 4*6 = 24
     - Factorial 5 : = 5 * 4! -> 5*24 = 120
    """
    if numero == 1 or numero == 0:
        print('Resultado factorial parcial :', numero, 'es: 1')
        return 1
    else:
        factorial_parcial = numero * factorial_de_un_numero(numero - 1)
        print('Resultado factorial parcial :', numero, f'es: {factorial_parcial}')
        return factorial_parcial

# Llamado de la funcion
# factorial_de_un_numero(5)


def potencia_de_un_numero(numero:int, potencia:int):
    """
    Imprime retorna el valor de la potencia de un numero, calculando el valor de manera recursiva
    :param numero: numero a elevar
    :param potencia: potencia del numero

    Caso base -> a^b = a * a^(b-1)
     - 2^3 -> 2*2*2 = 8
     - 6^2 -> 6*6 = 36
     - 4^4 -> 4*4*4*4*4 = 256
    """
    if potencia == 0:
        # print('Resultado potencia parcial1 :', numero, 'es: 1')
        return 1
    else:
        potencia_parcial = numero * potencia_de_un_numero(numero, potencia-1)
        # print('Resultado potencia parcial :', numero, f'es: {potencia_parcial}')
        return potencia_parcial

# Llamado de la funcion
print('*** Potencia de un Numero ***')
print(f'Resultado de la potencia: ', {potencia_de_un_numero(2,10)})
print(f'Resultado de la potencia: ', {potencia_de_un_numero(4,5)})
print(f'Resultado de la potencia: ', {potencia_de_un_numero(8,4)})