# Sistema de Gestión de Empleados
# Este programa demuestra los conceptos de POO: herencia, encapsulación y polimorfismo

class Empleado:
    def __init__(self, nombre, id):
        self._nombre = nombre  # Encapsulación: atributo protegido
        self._id = id  # Encapsulación: atributo protegido

    def get_nombre(self):
        return self._nombre

    def get_id(self):
        return self._id

    def calcular_salario(self):  # Método que será sobrescrito (polimorfismo)
        pass

    def mostrar_info(self):
        return f"ID: {self._id}, Nombre: {self._nombre}"


class EmpleadoTiempoCompleto(Empleado):  # Herencia
    def __init__(self, nombre, id, salario_anual):
        super().__init__(nombre, id)
        self.__salario_anual = salario_anual  # Encapsulación: atributo privado

    def calcular_salario(self):  # Polimorfismo: sobrescritura de método
        return self.__salario_anual / 12

    def mostrar_info(self):  # Polimorfismo: sobrescritura de método
        return f"{super().mostrar_info()}, Tipo: Tiempo Completo, Salario Mensual: ${self.calcular_salario():.2f}"


class EmpleadoPorHoras(Empleado):  # Herencia
    def __init__(self, nombre, id, tarifa_por_hora, horas_trabajadas):
        super().__init__(nombre, id)
        self.__tarifa_por_hora = tarifa_por_hora  # Encapsulación: atributo privado
        self.__horas_trabajadas = horas_trabajadas  # Encapsulación: atributo privado

    def calcular_salario(self):  # Polimorfismo: sobrescritura de método
        return self.__tarifa_por_hora * self.__horas_trabajadas

    def mostrar_info(self):  # Polimorfismo: sobrescritura de método
        return f"{super().mostrar_info()}, Tipo: Por Horas, Salario: ${self.calcular_salario():.2f}"


# Función para demostrar polimorfismo con argumentos múltiples
def imprimir_info_empleados(*empleados):
    for empleado in empleados:
        print(empleado.mostrar_info())


# Crear instancias de las clases
empleado1 = EmpleadoTiempoCompleto("Juan Pérez", "E001", 60000)
empleado2 = EmpleadoPorHoras("María García", "E002", 15, 160)

# Demostrar funcionalidad
print("Información de Empleados:")
imprimir_info_empleados(empleado1, empleado2)

# Acceder a métodos y atributos
print(f"\nNombre del Empleado 1: {empleado1.get_nombre()}")
print(f"Salario mensual del Empleado 1: ${empleado1.calcular_salario():.2f}")
print(f"Salario del Empleado 2: ${empleado2.calcular_salario():.2f}")