
# Realizar la suma de los 5 primeros numeros utilizando while

# suma = 0
# contador = 1
#
# while contador <= 5:
#     suma += contador
#     contador +=1
# print(f'La suma es: {suma}')

from random import randint

numberToSearch: int = randint(1,3)
ATTEMPTS = 5
myNumber = 0
myAttempts = 0

print('*** Adivina el numero Secreto ***')

while (myAttempts < ATTEMPTS) and (myNumber != numberToSearch):
        myNumber = int(input('Escribe un numero entre 1 y 30: '))
        myAttempts += 1
        if myNumber < numberToSearch:
            print('El numero secreto es mayor que: ',myNumber)
        elif myNumber > numberToSearch:
            print('El numero secreto es menor que: ',myNumber)
        elif numberToSearch == myNumber:
            print('El numero secreto es correcto: ',myNumber)
        elif myAttempts < ATTEMPTS:
            print(':( Numero de intentos alcanzados ',myNumber)
print('Fin del Juego')