
# option_menu: int = 0


def sistema_inventario():
    option_menu: int = 0
    lista_inventarios: list[dict[int, str, float, float]] = [
        {'id': 1, 'nombre': 'Cafe', 'precio': 1000, 'cantidad': 200},
        {'id': 2, 'nombre': 'Platano', 'precio': 200, 'cantidad': 1100},
        {'id': 3, 'nombre': 'Piña', 'precio': 10, 'cantidad': 300},
    ]

    while option_menu != 4:
        mostrar_menu()
        option_menu = int(input('Proporciona una opcion entre  (1-4): '))
        if option_menu == 1:
            mostrar_inventario(lista_inventarios)
        elif option_menu == 2:
            agregar_producto(lista_inventarios)
        elif option_menu == 3:
            buscar_producto_id(lista_inventarios)
        elif option_menu == 4:
            print('Hasta luego!')
            break
        else:
            print('Opcion invalida, proporciona una opcion valida')

def mostrar_menu():
    print(f'''\n --- Menu ---
        \t1. Mostrar Inventarios
        \t2. Agregar Producto
        \t3. Buscar Producto pot Id
        \t4. Salir
    ''')

def mostrar_producto(producto: dict[int,str,float,float]):
    print(
        f'Id: {producto.get('id')}, '
        f'Nombre: {producto.get("nombre")}, '
        f'Preco: ${producto.get("precio")}, '
        f'Cantidad: {producto.get("cantidad")}'
    )


def mostrar_inventario(listaProductos: list[dict]):
    if (len(listaProductos) == 0):
        print('No se encontraron productos en inventario')
    else:
        for producto in listaProductos:
            mostrar_producto(producto)


def agregar_producto(listaProductos: list[dict[int,str,float,float]]):
    id: int = len(listaProductos) + 1
    nombre: str = input('Ingrese el nombre del producto: ')
    precio: float = float(input('Ingrese el precio del producto: '))
    cantidad: float = float(input('Ingrese la cantidad del producto: '))
    listaProductos.append({'id': id, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
    print(f'Producto ID: {id} - Nombre: {nombre} -> Agregado.')


def buscar_producto_id(listaProductos: list[dict]):
    id: int = int(input('Ingrese el id del producto: '))
    producto = next((prod for prod in listaProductos if prod["id"] == id),'No')
    if(producto == 'No'):
        print(f'\nNo se a encontrado producto Id {id}')
    else:
        print(f'Informacion del producto encontrado')
        mostrar_producto(producto)
