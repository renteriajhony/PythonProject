# cadena = input('Numero: ')
# numero = 2
# resultado = numero + int(cadena)
# print(f'{resultado}')

print('*** Sistema de empleados***')
nombre_empleado = input('Ingresa el nombre del empleado: ')
edad_empleado = int(input('Ingresa la edad del empleado: '))
dalario_empleado = float(input('Ingresa el salario del empleado: '))
es_jefe_area = (input('El empleado es jefe de area (SI/NO): ')).upper() == 'SI'

print(f'Empleado: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario: {dalario_empleado}')
print(f'Jefe de area: {"SI" if es_jefe_area else"NO"}')