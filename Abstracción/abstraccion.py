# Abstracción: Definimos una clase base 'Vehiculo' que representa la abstracción de un vehículo general.
class Vehiculo:
    def __init__(self, marca, modelo, año):
        # Encapsulación: Los atributos 'marca', 'modelo' y 'año' están encapsulados.
        self.marca = marca
        self.modelo = modelo
        self.año = año

    # Método abstracto que debe ser implementado por las subclases.
    def encender(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    # Método que describe el vehículo.
    def describir(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")

