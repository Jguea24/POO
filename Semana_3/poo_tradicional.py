"""
Programación Tradicional:
Implementa una solución utilizando estructuras de funciones.
Define funciones para la entrada de datos diarios (temperaturas) y el cálculo del promedio semanal.
Organiza el código de manera lógica y funcional utilizando la programación tradicional.
"""
def ingresar_temperaturas():
    # Cargamos la lista de los días de la semana
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    # Creamos la lista para almacenar las temperaturas ingresadas
    temperaturas = []
    # Iteramos sobre cada día de la semana
    for dia in dias_semana:
        while True:
            try:
                # Solicitamos al usuario que ingrese la temperatura para el día actual
                temp = float(input(f"Ingrese la temperatura del {dia}: "))

                # Agregamos la temperatura a la lista
                temperaturas.append(temp)
                break
            except ValueError:
                # Mostramos un mensaje de error si el usuario ingresa un valor no válido
                print("Por favor, ingrese un número válido.")

    # Devolver la lista de temperaturas
    return temperaturas
def calcular_promedio(temperaturas):
    # Calculamos y devolvemos el promedio de las temperaturas
    return sum(temperaturas) / len(temperaturas)
def main():
    # Obtenemos las temperaturas ingresadas por el usuario
    temperaturas = ingresar_temperaturas()

    # Calculamos el promedio de las temperaturas
    promedio = calcular_promedio(temperaturas)
    # Mostramos el promedio semanal de las temperaturas con dos decimales
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")
# Ejecutamos la función principal si este script se ejecuta como el programa principal
if __name__ == "__main__":
    main()

