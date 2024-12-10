# edad = int(input('Ingresa tu edad: '))
#
# if edad >= 18:
#     print('Eres mayor de edad')
# elif edad > 12 and edad < 18:
#     print('Eres adolecente menor de edad')
# else: print('Eres menor de edad')

# print('*** Bienvenidos a la casa de los espejos')
# edad: int = int(input('Ingresa edad: '))
# isFear: bool = (input('Le temes a la oscuridad (Si/No): ')).lower().strip() == 'si'
#
# if edad >= 18 and not isFear:
#     print('Puedes entrar a la casa de los espejos')
# else: print('No puedes entrar a la casa de los espejos')

# # OPERADOR TERNARIO
# edad: int = int(input('Ingresa edad: '))
# es_adulto = 'Si' if edad >= 18 else 'No'
# print('Eres adulto:', es_adulto)

# Aplicacion de Salud y Fitness
print('**** Salud y Fitness ****')
META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASOS = 0.04
name = input("Digite su nombre: ")
steps = int(input('Ingrese cantidad de pasos del dia: '))

calorias_quemados = steps * CALORIAS_POR_PASOS
meta_alcanzada = (f'Cumpliste con la meta diaria de +{steps} diarios' if steps >= META_PASOS_DIARIOS else f'Te faltan {META_PASOS_DIARIOS-steps} pasos, para cumplir con la meta diaria de +{META_PASOS_DIARIOS} pasos diarios')


print(f'''
Hola {name},
\t Hoy caminaste {steps} pasos
\t Quemaste {calorias_quemados:.2f} calorias aproximadamente
\t {meta_alcanzada}
''')