from random import randint

#Generar numeros aleatorios importamos randint de random
# numberRamdom: int = randint(1, 10)
# print(f'Valor aleatorio: {numberRamdom}')

# Simulamos un dado de 6 caras
# dado = randint(1, 6)
# print(f'Valor dado: {dado}')

print('*** Sistema de generador de ID Unico ****')
name = input('Cual es tu nombre? ')
firshName = input('Cual es tu Apellido? ')
yearOfbirth = input('Cual es tu año de nacieminto (YYYY)? ')
numberRandom = randint(1000, 9999)

code = f'${name[0:2].strip()}{firshName[0:2].strip()}{yearOfbirth[2:].strip()}{numberRandom}'.upper()

print('\n')
print(f'Hola {name},')
print(f'\t\t Tu nuevo número de identificacion (ID) generado por el sistema es:')
print(f'\t\t {code}')
print(f'\t\t Felicidades!')

print(f'''\nHola {name},
\t\tTu nuevo número de identificacion (ID) generado por el sistema es:
\t\t{code}
\t\tFelicidades!
''')