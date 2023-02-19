import os
import helpers
import database as db


helpers.limpiar_pantalla()
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
            print("Listando clientes...\n")
            for cliente in db.Clientes.lista:
                print(cliente)

        if opcion == "2":
            print("Has seleccionado la opción 2")
            print("Buscando cliente...\n")
            cliente=db.Clientes.buscar(input("Introduzca el DNI del cliente: "))
            print(cliente) if cliente else print("No se ha encontrado el cliente")

        if opcion == "3":
            print("Has seleccionado la opción 3")
            print("Añadiendo cliente...\n")
            dni=helpers.leer_texto(3,3, "DNI(2 números y una letra):").upper()
            nombre=helpers.leer_texto(2,30, "Nombre:").capitalize()
            apellido=helpers.leer_texto(2,30, "Apellido:").capitalize()
            print("Estás creando un cliente con dni: " + dni + ", nombre: " + nombre + " y apellido: " + apellido)
            print("¿Estás seguro de que quieres crearlo?")
            opcion=input("S/N: ").upper()
            if opcion=="S":
                cliente=db.Clientes.crear(dni, nombre, apellido)
                print("Cliente creado correctamente")
            else:
                print("No se ha creado el cliente")

        if opcion == "4":
            print("Has seleccionado la opción 4")
            print("Modificando cliente...\n")
            dni=helpers.leer_texto(3,3, "DNI(2 números y una letra):").upper()
            cliente=db.Clientes.buscar(dni)
            if cliente:
                print("Estás modificando un cliente con dni: " + dni + ", nombre: " + cliente.nombre + " y apellido: " + cliente.apellido)
                print("¿Estás seguro de que quieres modificarlo?")
                opcion=input("S/N: ").upper()
                if opcion=="S":
                    nombre=helpers.leer_texto(
                        2, 30, f"Nombre(de 2 a 30 letras)[{cliente.nombre}]:").capitalize()
                    apellido=helpers.leer_texto(
                        2, 30, f"Apellido(de 2 a 30 letras)[{cliente.apellido}]:").capitalize()
                    db.Clientes.modificar(dni, nombre, apellido)
                    print("Cliente modificado correctamente")
                else:
                    print("No se ha modificado el cliente")
            else:
                print("No se ha encontrado el cliente")
                
        if opcion == "5":
            print("Has seleccionado la opción 5")
            print("Eliminando cliente...\n")
        if opcion == "6":
            print("Has seleccionado la opción 6")
            print("Saliendo...\n")
            break
        
        input("Pulse ENTER para continuar...")

        if opcion not in ("1", "2", "3", "4", "5", "6"):
            print("Opción incorrecta, por favor, introduzca una opción válida")
            input("Pulse ENTER para continuar...")
            os.system('cls')
        
