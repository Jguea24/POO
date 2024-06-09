# Polimorfismo: Implementamos el método 'encender' de manera específica para 'Coche'.
def encender(self):
    return "El coche está encendido"


# Polimorfismo: Sobrescribimos el método 'describir' para agregar detalles específicos.
def describir(self):
    super().describir()
    print(f"Puertas: {self.puertas}")


