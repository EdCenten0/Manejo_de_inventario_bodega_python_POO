import os
import time

def clientes():
    os.system("clear")
    print("Que desea hacer?: ")
    
    print("1. Agregar un cliente\n2. Leer los clientes\n3. Editar un cliente\n4. Eliminar un cliente\n5. Salir")
    opc = int(input())
    if(opc == 1):
        print
    elif(opc == 2):
        print
    elif(opc == 3):
        print
    elif(opc == 4):
        print
    elif(opc < 1 or opc > 5):
        print("Digite una opcion valida")
        time.sleep(3)
        os.system("clear")
        

    

def main():
    print("Menu")
    opc = 1
    while(opc > 0 and opc < 5 and opc != 4):
        print("Que desea hacer?: ")
        print("1. Clientes\n2. Empleados\n3. Productos\n4. Salir")
        opc = int(input())
        if(opc == 1):
            clientes()
        elif():
            print()

    

if __name__ == "__main__":
    main()