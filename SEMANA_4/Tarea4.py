class Libro:
    def __init__(self, titulo, autor, disponible=True):
        self.titulo = titulo        # Atributo para almacenar el título del libro
        self.autor = autor          # Atributo para almacenar el autor del libro
        self.disponible = disponible  # Atributo para controlar si el libro está disponible o no

    def __str__(self):
        estado = "disponible" if self.disponible else "prestado"
        return f"{self.titulo} por {self.autor} ({estado})"

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"Has prestado '{self.titulo}'.")
        else:
            print(f"'{self.titulo}' no está disponible para préstamo.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"Has devuelto '{self.titulo}'.")
        else:
            print(f"'{self.titulo}' ya está disponible.")

class Biblioteca:
    def __init__(self):
        self.catalogo = []  # Lista para almacenar los libros en el catálogo de la biblioteca

    def agregar_libro(self, libro):
        self.catalogo.append(libro)
        print(f"Agregado: {libro}")

    def buscar_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo.lower() == titulo.lower():  # Buscar el libro por título (ignorando mayúsculas)
                return libro
        return None

# Ejemplo de uso del sistema de biblioteca
if __name__ == "__main__":
    # Crear algunos libros
    libro1 = Libro("Python Crash Course", "Eric Matthes")
    libro2 = Libro("Mysql conexion con python", "Robert C. Martin")
    libro3 = Libro("Android Studio - Crea ti primer APP", "Andrew Hunt y David Thomas")

    # Crear una biblioteca y agregar libros
    biblioteca = Biblioteca()
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Prestar y devolver libros
    libro_prestado = biblioteca.buscar_libro("Python Crash Course")
    if libro_prestado:
        libro_prestado.prestar()

    libro_devuelto = biblioteca.buscar_libro("Clean Code")
    if libro_devuelto:
        libro_devuelto.devolver()

    # Mostrar estado actual de los libros en la biblioteca
    print("\nEstado actual de la biblioteca:")
    for libro in biblioteca.catalogo:
        print(libro)
