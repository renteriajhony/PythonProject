print('*** Argumentos variables ***')

# def superheroe_superpoderes(superheroe, nombre, *args, **kwargs):
#     """
#     Imprime detalle de supereroe
#     :param superheroe:
#     :param nombre:
#     :param args:
#     :param kwargs:
#     """
#     print(f'''
#     Superheroe: {superheroe}
#     Nombre: {nombre}
#     Argumentos: {args}
#     Kwargs: {kwargs}''')
#
# # Llamado de la funcion
# superheroe_superpoderes('SpiderMan', 'Peter', 'Instinto aracnido', 'Telaraña')
# superheroe_superpoderes('IronMan', 'Tony Stark','Armadura',edad= 47, empresa = 'Marvel',)

def imprimir_detalle_persona(**kwargs):
    print('*** Valores recibidos ***')
    for key, value in kwargs.items():
            print(f'{key} : {value}')
imprimir_detalle_persona(nombre='Fidel', apellido='Castro', sexo='M')
imprimir_detalle_persona(car= 'los')
