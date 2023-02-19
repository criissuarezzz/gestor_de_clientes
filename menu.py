import os 
def iniciar():
    while True:
        os.system('cls')

        print("=========================")
        print("  Bienvenido al manager  ")
        print("=========================")
        print(" Escriba el número de la ")
        print("opción que desea ejecutar")
        print("=========================")
        print("1-> Listar clientes      ")
        print("2-> Buscar cliente       ")
        print("3-> Añadir cliente       ")
        print("4-> Modificar cliente    ")
        print("5-> Eliminar cliente     ")
        print("6-> Salir                ")
        print("=========================")

        opcion = input("Opción: ")
        os.system('cls')

        if opcion == "1":
            print("Has seleccionado la opción 1")
            print("Listando clientes...")
        if opcion == "2":
            print("Has seleccionado la opción 2")
            print("Buscando cliente...")
        if opcion == "3":
            print("Has seleccionado la opción 3")
            print("Añadiendo cliente...")
        if opcion == "4":
            print("Has seleccionado la opción 4")
            print("Modificando cliente...")
        if opcion == "5":
            print("Has seleccionado la opción 5")
            print("Eliminando cliente...")
        if opcion == "6":
            print("Has seleccionado la opción 6")
            print("Saliendo...")
            break
        
        input("Pulse ENTER para continuar...")
