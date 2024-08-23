
"""  Desarrollar un sistema de gestión de inventarios simple para una tienda, que permita añadir, actualizar,
eliminar y buscar productos utilizando una estructura de datos personalizada."""

# Creamos nuestra la clase Producto
class Producto:
    # Creamos el Constructor de la clase Producto
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id  # Identificador único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible del producto
        self.precio = precio  # Precio del producto

    # Métodos Getters para acceder y modificar los atributos
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos Setters para acceder y modificar los atributos
    def set_id(self, id):
        self.id = id

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # Método para representar el objeto Producto como una cadena de texto
    def __str__(self):
        return f'ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}'


# Creamos la  clase Inventario
class Inventario:
    # Creamo un Constructor de la clase Inventario
    def __init__(self):
        self.productos = []  # Lista para almacenar los productos en el inventario

    # Método para añadir un nuevo producto al inventario
    def añadir_producto(self, producto):
        # Verificar si el ID del producto es único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID del producto ya existe.")
                return
        self.productos.append(producto)  # Añadir el producto a la lista
        print("Producto añadido exitosamente.")

    # Método para eliminar un producto del inventario por su ID
    def eliminar_producto(self, id):
        for p in self.productos:
            if p.get_id() == id:
                self.productos.remove(p)  # Eliminar el producto de la lista
                print("Producto eliminado exitosamente.")
                return
        print("Error: Producto no encontrado.")  # Si no se encuentra el producto

    # Método para actualizar la cantidad o el precio de un producto por su ID
    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)  # Actualizar la cantidad si se proporciona
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)  # Actualizar el precio si se proporciona
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")  # Si no se encuentra el producto

    # Método para buscar productos por su nombre (o parte del nombre)
    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for p in resultados:
                print(p)  # Imprimir todos los productos que coincidan con el nombre
        else:
            print("No se encontraron productos con ese nombre.")  # Si no se encuentra ningún producto

    # Método para mostrar todos los productos en el inventario
    def mostrar_productos(self):
        if self.productos:
            for p in self.productos:
                print(p)  # Imprimir todos los productos
        else:
            print("El inventario está vacío.")  # Si no hay productos en el inventario


# Función para mostrar el menú interactivo en la consola
def menu():
    inventario = Inventario()  # Crear una instancia de Inventario

    while True:
        # Mostrar el menú de opciones
        print("\n=== Menú de Gestión de Inventario ===")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto por Nombre")
        print("5. Mostrar Todos los Productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")  # Leer la opción seleccionada por el usuario

        if opcion == '1':
            # Opción para añadir un nuevo producto
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)  # Crear un objeto Producto
            inventario.añadir_producto(producto)  # Añadir el producto al inventario

        elif opcion == '2':
            # Opción para eliminar un producto
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)  # Eliminar el producto por su ID

        elif opcion == '3':
            # Opción para actualizar un producto
            id = input("Ingrese el ID del producto a actualizar: ")
            nueva_cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
            nuevo_precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")

            # Convertir las entradas en valores numéricos si se proporcionaron
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            inventario.actualizar_producto(id, nueva_cantidad, nuevo_precio)  # Actualizar el producto

        elif opcion == '4':
            # Opción para buscar un producto por su nombre
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)  # Buscar el producto por nombre

        elif opcion == '5':
            # Opción para mostrar todos los productos
            inventario.mostrar_productos()  # Mostrar todos los productos en el inventario

        elif opcion == '6':
            # Opción para salir del menú
            print("Saliendo del sistema de inventario.")
            break  # Salir del bucle y finalizar el programa

        else:
            # Mensaje para opción no válida
            print("Opción no válida. Intente nuevamente.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu()  # Iniciar el menú interactivo
