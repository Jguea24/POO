class Archivo:
    def __init__(self, nombre):
        """
        Constructor de la clase Archivo.
        Se llama automáticamente cuando se crea una nueva instancia.
        :param nombre: Nombre del archivo a abrir
        """
        self.nombre = nombre
        self.archivo = None
        print(f"Constructor: Inicializando archivo '{self.nombre}'")
        try:
            self.archivo = open(self.nombre, 'w')
            print(f"Archivo '{self.nombre}' abierto con éxito")
        except IOError:
            print(f"Error al abrir el archivo '{self.nombre}'")

    def escribir(self, texto):
        """
        Método para escribir en el archivo.

        :param texto: Texto a escribir en el archivo
        """
        if self.archivo:
            self.archivo.write(texto)
            print(f"Texto escrito en '{self.nombre}'")
        else:
            print("Error: El archivo no está abierto")
    def __del__(self):
        """
        Destructor de la clase Archivo.
        Se llama automáticamente cuando el objeto está a punto de ser destruido.
        """
        print(f"Destructor: Limpiando recursos para '{self.nombre}'")
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre}' cerrado")
# Uso de la clase
def main():
    # Creación de una instancia de Archivo (llama al constructor)
    mi_archivo = Archivo("ejemplo.txt")
    # Uso del objeto
    mi_archivo.escribir("El constructor se define mediante el método especial __init__.! \n")
    mi_archivo.escribir("El destructor puede ser útil para tareas como cerrar conexiones a bases de datos o archivos!")
    # El destructor se llamará automáticamente cuando el objeto salga de ámbito
    print("Fin del programa")

if __name__ == "__main__":
    main()