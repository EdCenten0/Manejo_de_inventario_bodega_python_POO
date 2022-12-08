from persona import Persona

class Empleado(Persona):
    puesto = str
    id_empleado = str
    salario = float

    def __init__(self, puesto, id_empleado, salario):
        self.puesto = puesto
        self.id_empleado = id_empleado
        self.salario = salario

    def __init__(self):
        self.puesto
        self.id_empleado
        self.salario
        