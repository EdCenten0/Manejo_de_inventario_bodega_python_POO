from persona import Persona

class Cliente(Persona):
    id_cliente = str

    def __init__(self, id_cliente):
        self.id_cliente = id_cliente

    def __init__(self):
        self.id_cliente

    def agregarCliente(self):
        clientes = []
        
        print("Ingrese el nombre del cliente a agregar: ")
        self.nombre = input()
        print("Ingrese la cedula")