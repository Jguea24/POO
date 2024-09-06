""" Desarrollar un sistema para gestionar una biblioteca digital.
El sistema permitirá administrar los libros disponibles,
las categorías de libros, los usuarios registrados y el historial
de préstamos."""
# Clase Libro: representa un libro con atributos título, autor, categoría e ISBN
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self._titulo_autor = (titulo, autor)  # Tupla para título y autor, inmutable
        self.categoria = categoria
        self.isbn = isbn

    @property
    def titulo(self):
        return self._titulo_autor[0]

    @property
    def autor(self):
        return self._titulo_autor[1]

    def __str__(self):
        return f"{self.titulo} por {self.autor} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# Clase Usuario: representa a un usuario con ID único, nombre y lista de libros prestados
class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = []
        # Lista para agreagr los libros prestados

    # Creamos el Método para añadir un libro a la lista de préstamos
    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    # Método para devolver un libro
    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


# Clase Biblioteca: gestiona libros, usuarios y préstamos
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario para almacenar libros (ISBN -> Libro)
        self.usuarios_registrados = {}  # Diccionario para usuarios (ID usuario -> Usuario)
        self.libros_prestados = {}  # Diccionario para préstamos (ISBN -> ID usuario)

    # Método para añadir un libro
    def anadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro añadido: {libro}")
        else:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")

    # Método para quitar un libro
    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print(f"No se encontró el libro con ISBN {isbn}.")

    # Método para registrar un usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    # Método para dar de baja a un usuario
    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            del self.usuarios_registrados[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"No se encontró al usuario con ID {id_usuario}.")

    # Método para prestar un libro
    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.libros_disponibles:
            print(f"El libro con ISBN {isbn} no está disponible.")
            return

        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
            return

        if isbn in self.libros_prestados:
            print(f"El libro con ISBN {isbn} ya está prestado.")
            return

        libro = self.libros_disponibles[isbn]
        usuario = self.usuarios_registrados[id_usuario]
        usuario.prestar_libro(libro)
        self.libros_prestados[isbn] = id_usuario
        print(f"Libro prestado: {libro} al usuario {usuario.nombre}")

    # Método para devolver un libro
    def devolver_libro(self, isbn, id_usuario):
        if isbn not in self.libros_prestados:
            print(f"El libro con ISBN {isbn} no está prestado.")
            return

        if self.libros_prestados[isbn] != id_usuario:
            print(f"El libro con ISBN {isbn} no está prestado al usuario con ID {id_usuario}.")
            return

        usuario = self.usuarios_registrados[id_usuario]
        libro = self.libros_disponibles[isbn]
        usuario.devolver_libro(libro)
        del self.libros_prestados[isbn]
        print(f"Libro devuelto: {libro} por el usuario {usuario.nombre}")

    # Método para buscar libros
    def buscar_libro(self, criterio, valor):
        resultados = [libro for libro in self.libros_disponibles.values() if getattr(libro, criterio) == valor]
        if resultados:
            print(f"Libros encontrados con {criterio}: {valor}")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros con {criterio}: {valor}")

    # Método para listar libros prestados
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"El usuario {usuario.nombre} no tiene libros prestados.")
        else:
            print(f"No se encontró al usuario con ID {id_usuario}.")


# Función principal para la interacción del usuario
def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n--- Menú de Biblioteca de Johnny Grefa ---")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            categoria = input("Ingrese la categoría del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.anadir_libro(libro)

        elif opcion == "2":
            isbn = input("Ingrese el ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            id_usuario = input("Ingrese el ID del usuario: ")
            nombre = input("Ingrese el nombre del usuario: ")
            usuario = Usuario(id_usuario, nombre)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            id_usuario = input("Ingrese el ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == "5":
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            biblioteca.prestar_libro(isbn, id_usuario)

        elif opcion == "6":
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            biblioteca.devolver_libro(isbn, id_usuario)

        elif opcion == "7":
            criterio = input("Buscar por 'titulo', 'autor' o 'categoria': ")
            valor = input(f"Ingrese el {criterio} a buscar: ")
            biblioteca.buscar_libro(criterio, valor)

        elif opcion == "8":
            id_usuario = input("Ingrese el ID del usuario: ")
            biblioteca.listar_libros_prestados(id_usuario)

        elif opcion == "9":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el menú de la biblioteca
menu()

