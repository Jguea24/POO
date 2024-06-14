""" Desarrollar habilidades prácticas en la Programación Tradicional yla Programación Orientada
a Objetos (POO) mediante la implementació de un programa en Python para determinar el promedio semanal del clima."""

# Iniciamos a dessarrolla  algoritmo.
class ClimaSemanal:
    def __init__(self):
        # Inicializamos una lista vacía para almacenar las temperaturas
        self.temperaturas = []
        # Creamos la lista de los días de la semana
        self.dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

    def ingresar_temperaturas(self):
        # Solicitamos  al usuario que ingrese la temperatura para cada día de la semana
        for i in range(7):
            while True:
                try:
                    # Intenta convertir la entrada del usuario a un número flotante
                    temp = float(input(f"Ingrese la temperatura del {self.dias_semana[i]}: "))
                    # Si la conversión tiene éxito, agrega la temperatura a la lista
                    self.temperaturas.append(temp)
                    break
                except ValueError:
                    # Si ocurre un error de valor (entrada no numérica), muestra un mensaje de error
                    print("Por favor, ingrese un número válido.")

    def calcular_promedio(self):
        # Si la lista de temperaturas está vacía, retorna 0 para evitar división por cero
        if not self.temperaturas:
            return 0
        # Calculamos el promedio sumando las temperaturas y dividiendo por el número de temperaturas
        return sum(self.temperaturas) / len(self.temperaturas)

    def mostrar_promedio(self):
        # Calcula el promedio de las temperaturas
        promedio = self.calcular_promedio()
        # Muestramos el promedio formateado con dos decimales
        print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")

def main():
    # Creamos una instancia de la clase ClimaSemanal
    clima = ClimaSemanal()
    # Llamamos al método para ingresar las temperaturas
    clima.ingresar_temperaturas()
    # Llamamos al método para mostrar el promedio de las temperaturas
    clima.mostrar_promedio()

# Este bloque asegura que el código dentro de él solo se ejecuta si el script se ejecuta directamente
if __name__ == "__main__":
    main()


