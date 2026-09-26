inventario = []

def agregar_producto():
    nombre_producto = input("Ingrese el nombre del producto: ")
    while True:
        try:
            cantidad_producto = int(input("Ingrese la cantidad del producto: "))
            break
        except ValueError:
            print('Valor invalido. Por favor ingresa un numero entero.')
    while True:
        try:
            presio_producto = float(input("Ingrese el presio del producto: $"))
            break
        except ValueError:
            print('Valor invalido.')
    producto = {'nombre': nombre_producto,'cantidad': cantidad_producto,'presio': presio_producto}
    inventario.append(producto)
    print('Producto agregado correctamente.')



def listar_productos():
    for producto in inventario:
        print(f"Producto: {producto['nombre']}")
        print(f"Cantidad: {producto['cantidad']}")
        print(f"Presio: ${producto['presio']}")


def buscar_producto():
    producto_buscado = input("Ingrese el nombre del producto: ")
    for producto in inventario:
        if not producto['nombre'].lower() in inventario:
            print(f'El producto {producto_buscado} no existe')
        else:
            print(f'Producto: {producto['nombre']}')
            print(f'Cantidad: {producto['cantidad']}')
            print(f'Presio: ${producto['presio']}')
            break
    if not inventario:
        print('El inventario esta vacio')

