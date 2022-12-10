from persona import Persona
from linked_list import Linked_list

class Cliente(Persona):
    id_cliente = str
    lista_cliente =  Linked_list()
    

    def __init__(self, id_cliente):
        self.id_cliente = id_cliente

    def __init__(self):
        self.id_cliente

    def agregar_clientes_lista(self, nombre, cedula, numero_telefonico, edad, id_cliente):
        self.lista_cliente.agregar(nombre)
        self.lista_cliente.agregar(cedula)
        self.lista_cliente.agregar(numero_telefonico)
        self.lista_cliente.agregar(edad)
        self.lista_cliente.agregar(id_cliente)


    def agregarCliente(self):
        
        
        print("Ingrese el nombre del cliente a agregar: ")
        self.nombre = input()
        print("Ingrese la cedula")
        self.cedula = input()
        print("Ingrese su numero telefonico: ")
        self.numero_telefonico = input()
        print("Ingrese su edad: ")
        self.edad = int(input())
        print("Ingrese el ID del cliente: ")
        self.id_cliente = input()

        self.agregar_clientes_lista(self.nombre, self.cedula, self.numero_telefonico, self.edad, self.id_cliente)
    

    def leerClientes(self):
        cadena_de_nombres = self.lista_cliente.__str__()
        return cadena_de_nombres

    
    def eliminarClientes(self):
        print


    
