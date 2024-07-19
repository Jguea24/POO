import os
# Importa el módulo os para interactuar con el sistema operativo

# Función para mostrar el contenido de un archivo
def mostrar_codigo(ruta_script):
    # Convierte la ruta del script a una ruta absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        # Abre el archivo en modo lectura
        with open(ruta_script_absoluta, 'r') as archivo:
            # Imprime el nombre del archivo y su contenido
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        # Si el archivo no se encuentra, imprime un mensaje de error
        print("El archivo no se encontró.")
    except Exception as e:
        # Si ocurre cualquier otro error, imprime el error
        print(f"Ocurrió un error al leer el archivo: {e}")

# Función para mostrar el menú y manejar las elecciones del usuario
def mostrar_menu():
    # Obtiene la ruta del directorio donde se encuentra el script principal
    ruta_base = os.path.dirname(__file__)

    # Diccionario con las opciones del menú y sus rutas correspondientes
    opciones = {
        '1': 'scripts/ejemplo1.py',
        '2': 'scripts/ejemplo2.py'
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {os.path.basename(opciones[key])}")
        print("0 - Salir")

        # Solicita al usuario que elija una opción
        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            # Si el usuario elige '0', se sale del bucle y termina el programa
            break
        elif eleccion in opciones:
            # Si el usuario elige una opción válida, obtiene la ruta del script correspondiente
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            # Muestra el código del script seleccionado
            mostrar_codigo(ruta_script)
        else:
            # Si la opción no es válida, imprime un mensaje de error
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecuta el menú si el script se está ejecutando directamente
if __name__ == "__main__":
    mostrar_menu()
