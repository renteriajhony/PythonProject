
# lista = [1,2,3,4,5,6,7,8,9,10]
# print(lista)
# lista.pop(-1)
# print(lista)
# lista.insert(2,10)
# print(lista)
# del lista[0]
# print(lista)
#
# for element in lista:
#     print(element, end =  '')
# print('\n')
# listaHete = [1,True,['a','e'],{'name': 'Juan'}]
# print(listaHete)
# for element in listaHete:
#     print(element)


# tuplas = ('a','e','i','o','u',[1,2,3,4,5])
# print(tuplas)
# for tupla in tuplas:
#     print(tupla, end=' ')
# print('\n')
# print(len(tuplas[5]))
#
# tuplas[5][0] = 10
# print(tuplas)

# # Desempaquetado de tuplas
# producto = ('UP100', 'Camisa', 1500)
#
# id , descripcion, precio = producto
# print(producto)
# print(precio)
# precio = 5000
# print(precio)
# print(producto)

# Sets en python
# numeros = {1,2,2,3,4,5,6}
# print(numeros)

# a = {1,2,3,4}
# b = {3,4,5,6}
#
# union = a.union(b) # a | b
# print(union)
#
# intersection = a.intersection(b) # a & b
# print(intersection)
#
# diferencia = a.difference(b) # a - b
# print(diferencia)


# print('*** Agenda de contactos***')
# contactos = {}
# nombre = ''
#
# while nombre != ';':
#         nombre = input('Nombre: ')
#         if nombre != ';':
#             telefono = input('Telefono: ')
#             email = input('Email: ')
#             direccion = input('Direccion: ')
#             contactos[nombre] = {
#                 'telefono': telefono,
#                 'email': email,
#                 'direccion': direccion,
#             }
#             print('\n')
# print(contactos.keys())

print('*** Sistema de inventarios ***')
inventario = []
prodc = int(input('Ingrese cantidad de productos a ingresar: '))

for i in range(prodc):
    id = i+1
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = float(input('Cantidad: '))
    inventario.append({
        'id': id,
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad,
    })
    print('\n')

print(f'Inventario Inicial {inventario}')

idBuscar = int(input('Ingrese id de producto a buscar: '))
productoEncontrado = None
for producto in inventario:
    if producto['id'] == idBuscar:
        productoEncontrado = producto
        break
print(productoEncontrado)