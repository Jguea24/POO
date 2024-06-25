"""Snake_case son nombres de variables y funciones
que usan minúsculas y separan las palabras con guiones bajos (_). """
# Definimos una clase para presentar a un estudiante
class Estudiante:
    def __init__(self, nombre, edad, promedio_notas):
        self.nombre = nombre  # Tipo de dato string
        self.edad = int(edad)  # Tipo de dato integer, convertimos a entero
        self.promedio_notas = float(promedio_notas)  # Tipo de dato float, convertimos a flotante
# Creamos una función para agregar un nuevo estudiante al registro
def agregar_estudiante(registro, nombre, edad, promedio_notas):
    nuevo_estudiante = Estudiante(nombre, edad, promedio_notas)
    registro.append(nuevo_estudiante)
# Creamos una función para mostrar la lista de estudiantes registrados
def mostrar_estudiantes(registro):
    for estudiante in registro:
        print(f'Nombre: {estudiante.nombre}, Edad: {estudiante.edad}, Promedio: {estudiante.promedio_notas}')
# Creamos una función para calcular el promedio de edades de los estudiantes
def calcular_promedio_edad(registro):
    total_edad = sum(estudiante.edad for estudiante in registro)
    promedio_edad = total_edad / len(registro) if registro else 0
    return promedio_edad
# Creamos la función principal del programa donde nos permitirá ingresar los datos.
def main():
    registro_estudiantes = []
    continuar = True
    while continuar:
        print("\nSeleccione una de las opciones:")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes agregados")
        print("3. Calcular el promedio de edad de los estudiantes")
        print("4. Salir")
        opcion = input("Ingrese una de las opciones para ejecutar el programa: ")
        if opcion == '1':
            nombre = input("Ingrese el nombre del estudiante: ")
            edad = input("Ingrese la edad del estudiante: ")
            promedio_notas = input("Ingrese el promedio de notas del estudiante: ")
            agregar_estudiante(registro_estudiantes, nombre, edad, promedio_notas)
        elif opcion == '2':
            mostrar_estudiantes(registro_estudiantes)
        elif opcion == '3':
            promedio_edad = calcular_promedio_edad(registro_estudiantes)
            print(f'El promedio de edad de los estudiantes es: {promedio_edad:.2f}')
        elif opcion == '4':
            continuar = False
        else:
            print("¡La opción que ingresó no es válida!!😮😮😮😮!! Intente de nuevo.")
if __name__ == "__main__":
    main()
