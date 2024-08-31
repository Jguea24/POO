""" Desarrollar un sistema avanzado de gestión de inventarios para una tienda,
 que incorpore las colecciones en POO para un manejo eficiente de los ítems
 del inventario y almacene la información del inventario en archivos."""
# Clase Producto
import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["id_producto"], data["nombre"], data["cantidad"], data["precio"])


class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        if producto.id_producto in self.productos:
            print(f"El producto con ID {producto.id_producto} ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado.")
        else:
            print(f"No se encontró un producto con ID {id_producto}.")

    def mostrar_todos_los_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("No hay productos en el inventario.")

    def guardar_inventario_json(self, archivo):
        data = [producto.to_dict() for producto in self.productos.values()]
        with open(archivo, 'w') as f:
            json.dump(data, f, indent=4)
        print("Inventario guardado correctamente en formato txt.")

    def cargar_inventario_json(self, archivo):
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)
                for producto_data in data:
                    producto = Producto.from_dict(producto_data)
                    self.añadir_producto(producto)
            print("Inventario cargado correctamente desde archivo txt.")
        except FileNotFoundError:
            print(f"No se encontró el archivo {archivo}. Se iniciará un inventario vacío.")


def mostrar_menu():
    print("Sistema de Gestión de Inventario")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Mostrar todos los productos")
    print("4. Guardar inventario")
    print("5. Cargar inventario")
    print("6. Salir")


def main():
    inventario = Inventario()
    archivo = "inventario.txt"

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            inventario.mostrar_todos_los_productos()

        elif opcion == "4":
            inventario.guardar_inventario_json(archivo)

        elif opcion == "5":
            inventario.cargar_inventario_json(archivo)

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()