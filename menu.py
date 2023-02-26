import os
import helpers
import database as db

#python run.py -t

def iniciar():    #funcion para iniciar el menu
    while True:
        helpers.limpiar_pantalla()

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

        opcion = input("Opción: ")   #leemos la opcion que queremos ejecutar
        helpers.limpiar_pantalla()  #limpiamos la pantalla

        if opcion == "1":     #si la opcion es 1, mostramos un mensaje y listamos los clientes
            print("Has seleccionado la opción 1")
            print("Listando clientes...\n")
            for cliente in db.Clientes.lista:    #para el cliente en la base de datos(db) de la clase Clientes, en la lista
                print(cliente)

        elif opcion == "2":         #si la opcion es 2, mostramos un mensaje y buscamos el cliente 
            print("Has seleccionado la opción 2")   
            print("Buscando cliente...\n")
            dni=helpers.leer_texto(3,3, "DNI(2 números y una letra):").upper()    #leemos el dni del cliente y  lo pasamos a mayusculas
            cliente=db.Clientes.buscar(dni)    #buscamos el cliente en la base de datos
            print(cliente) if cliente else print("No se ha encontrado el cliente") 

        elif opcion == "3":
            print("Has seleccionado la opción 3")
            print("Añadiendo cliente...\n")
            dni=None  #inicializamos la variable dni a None, lo que implica que no tiene valor
            while True:   
                dni=helpers.leer_texto(3,3, "DNI(2 números y una letra):").upper()   #leemos el dni del cliente y  lo pasamos a mayusculas
                if helpers.dni_valido(dni, db.Clientes.lista):   #comprobamos que el dni cumple el formato y que no se repite
                    break
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

        elif opcion == "4":
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
                
        elif opcion == "5":
            print("Has seleccionado la opción 5")
            print("Eliminando cliente...\n")
            dni=helpers.leer_texto(3,3, "DNI(2 números y una letra):").upper()
            print("Cliente borrado correctamente") if db.Clientes.borrar(dni) else print("No se ha encontrado el cliente")

        elif opcion == "6":
            print("Has seleccionado la opción 6")
            print("Saliendo...\n")
            break
        
        input("Pulse ENTER para continuar...")

        if opcion not in ("1", "2", "3", "4", "5", "6"):
            print("Opción incorrecta, por favor, introduzca una opción válida")
            input("Pulse ENTER para continuar...")
            os.system('cls')
        
        
