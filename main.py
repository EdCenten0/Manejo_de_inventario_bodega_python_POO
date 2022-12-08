import os

def main():
    print("Menu")
    opc = 1
    while(opc > 0 and opc < 5 and opc != 4):
        print("Que desea hacer?: ")
        print("1. Clientes\n2. Empleados\n3. Productos\n4. Salir")
        opc = int(input())
        if(opc == 1):
            os.system("clear")
            print("Que desea hacer?: ")
            print("1. Agregar un cliente\n2. Leer los clientes\n3. Editar un cliente\n 4. Eliminar un cliente")
        elif():
            print()

    

if __name__ == "__main__":
    main()