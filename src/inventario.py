import json
import os

def cargar_json(ruta_archivo, valor_defecto=None):
    if valor_defecto is None:
        valor_defecto = []

    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return valor_defecto
    except json.JSONDecodeError:
        print(f"⚠️ Error: '{ruta_archivo}' está corrupto. Se usará un respaldo vacío.")
        return valor_defecto
    except OSError:
        print(f"❌ Error de sistema al leer '{ruta_archivo}': ")
        return valor_defecto



def guardar_json(datos, ruta_archivo):
    ruta_temporal = f"{ruta_archivo}.tmp"
    try:
        with open(ruta_temporal, mode='w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, ensure_ascii = False, indent = 4)

        os.replace(ruta_temporal, ruta_archivo)
        return True
    except (OSError, TypeError) as e:
        print(f"❌ No se pudo guardar '{ruta_archivo}': {e}")
        if os.path.exists(ruta_temporal):
            os.remove(ruta_temporal)
        return False

inventario = cargar_json('inventario.json', valor_defecto=[])


def guardar_inventario():
    guardar_json(inventario, 'inventario.json')


def menu():
    print("\n--- Menu Inventario ---")
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Eliminar producto")
    print("4. Listar productos")
    print("5. Buscar producto")
    print("6. Salir")
    try:
        return int(input("Selecciona una opcion: "))
    except ValueError:
        print("Valor invalido. Ingresa un numero.")
        return 0




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
            precio_producto = float(input("Ingrese el precio del producto: $"))
            break
        except ValueError:
            print('Valor invalido.')
    producto = {'nombre': nombre_producto,'cantidad': cantidad_producto,'precio': precio_producto}
    inventario.append(producto)
    guardar_inventario()
    print('Producto agregado correctamente.')



def actualizar_producto():
    if not inventario:
        print("El inventario esta vacio")
        return

    nombre_producto = input("Ingrese el nombre del producto a actualizar: ")
    producto_encontrado = False

    for producto in inventario:
        if producto['nombre'].lower() == nombre_producto.lower():
            print(f"\nProducto encontrado: {producto['nombre']}")
            print(f"Cantidad actual: {producto['cantidad']}")
            print(f"Precio actual: ${producto['precio']}")

            opcion = input("Que desea actualizar? (C = Cantidad, P = Precio): ").lower()

            if opcion == "c":
                try:
                    nueva_cantidad = int(input("Ingrese la nuevo cantidad: "))
                    producto['cantidad'] = nueva_cantidad
                except ValueError:
                    print('Valor invalido. No se actualizo la cantidad.')
            elif opcion == "p":
                try:
                    nuevo_precio = float(input("Ingrese el nuevo precio: $"))
                    producto['precio'] = nuevo_precio
                except ValueError:
                    print('Valor invalido. No se actualizo el precio.')
            else:
                print("Opcion invalida. No se actualizo nada.")

            guardar_inventario()
            print(f'Producto {nombre_producto} actualizado correctamente.')
            producto_encontrado = True
            break
    if not producto_encontrado:
        print(f"El producto {nombre_producto} no existe.")




def eliminar_producto():
    if not inventario:
        print("El inventario esta vacio")
        return

    nombre_producto = input("Ingrese el nombre del producto: ")
    producto_encontrado = False

    for producto in inventario:
        if producto['nombre'].lower() == nombre_producto.lower():
            inventario.remove(producto)
            guardar_inventario()
            print(f'El producto {nombre_producto} eliminado correctamente.')
            producto_encontrado = True
            break
    if not producto_encontrado:
        print(f'El producto {nombre_producto} no existe.')



def listar_productos():
    if not inventario:
        print("El inventario esta vacio")
        return
    print("\nInventario disponible:")
    for producto in inventario:
        print(f"\nProducto: {producto['nombre']}")
        print(f"Cantidad: {producto['cantidad']}")
        print(f"Precio: ${producto['precio']}\n")


def buscar_producto():
    producto_buscado = input("Ingrese el nombre del producto: ")
    producto_encontrado = False
    for producto in inventario:
        if producto['nombre'].lower() == producto_buscado.lower():
            print(f'Producto: {producto['nombre']}')
            print(f'Cantidad: {producto['cantidad']}')
            print(f'Precio: ${producto['precio']}')
            producto_encontrado = True
            break
    if not inventario:
        print('El inventario esta vacio')
    elif not producto_encontrado:
        print(f'El producto {producto_buscado} no existe')


if __name__ == '__main__':
    while True:
        opcion = menu()

        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            actualizar_producto()
        elif opcion == 3:
            eliminar_producto()
        elif opcion == 4:
            listar_productos()
        elif opcion == 5:
            buscar_producto()
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print('Opcion invalida. Vuelve a intentarlo')