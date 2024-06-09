# Herencia: Definimos una subclase 'Coche' que hereda de 'Vehiculo'.
class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        # Llamamos al constructor de la clase base para inicializar los atributos comunes.
        super().__init__(marca, modelo, año)
        # Atributo específico de la clase 'Coche'.
        self.puertas = puertas


# Herencia: Definimos una subclase 'Moto' que hereda de 'Vehiculo'.
class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        # Llamamos al constructor de la clase base para inicializar los atributos comunes.
        super().__init__(marca, modelo, año)
        # Atributo específico de la clase 'Moto'.
        self.tipo = tipo