
# columnsNumber = int(input("Enter the number of columns: "))
#
# for fila in range(columnsNumber+1):
#     espacios_blanco = ' ' * (columnsNumber - fila)
#     asteriscoas = '' * (2*fila -1)
#     print(f'{espacios_blanco}{asteriscoas}')

#    *
#   ***
#  *****
# *******
#*********

#Numero de * por iteracion
# 0 = 1
# 1 = 3
# 2 = 5
# 3 = 7
# 4 = 9

#Numero de espacios por iteracion
# 0 = 4
# 1 = 3
# 2 = 2
# 3 = 1
# 4 = 0


cadena = 'Hola Mundo como estas el triangulo'
contador = 0
_vocales = ['a','e','i','o','u']
for i in cadena:
    if _vocales.__contains__(i):
        contador += 1
print(contador)