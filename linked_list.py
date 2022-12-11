from nodo import Node

class Linked_list:
    def __init__(self):
        self.First = None
        self.Size = 0

    def agregar(self, value):
        mi_nodo = Node(value)
        if(self.Size == 0 ):
            self.First = mi_nodo
        else:
            current = self.First
            while (current.next != None):
                current = current.next
            current.next = mi_nodo
        self.Size += 1
        return mi_nodo
    
    def eliminar(self, value):
        if(self.Size == 0):
            return False;
        else:
            current = self.First
            try:
                while current.next.value !=  value:
                    
                    current = current.next 
                deleted_node = current.next
                current.next = deleted_node.next
            except ArithmeticError:
                return False
        self.Size -= 1

        return deleted_node

    def __len__(self):
        return self.Size
    
    def __str__(self):
        string = "------------------------------------------------"
        current = self.First
        conteo = 0
        for i in range(len(self)):
            if(i%5==0 or i == 0):
                
                conteo += 1
                string += "\nCliente " + str(conteo) + ":\n"
                
            string += str(current)
            if i != len(self) - 1:
                string += str(", ")
            current = current.next
        
        string += str("\n------------------------------------------------")

        return string