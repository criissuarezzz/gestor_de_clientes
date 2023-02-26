import csv
import config


class Cliente:     #crea la clase cliente, con sus atributos
    def __init__(self, dni, nombre, apellido):   #constructor de la clase con nombre, apellido y dni
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):     #método para imprimir los datos del cliente
        return f"({self.dni}) {self.nombre} {self.apellido}"

    def to_dict(self):    #método para convertir los datos del cliente en un diccionario
        return {'dni': self.dni, 'nombre': self.nombre, 'apellido': self.apellido}


class Clientes:   #crea la clase clientes para gestionar los clientes
    lista = []    #crea una lista vacía
    with open(config.DATABASE_PATH, newline='\n') as fichero:   #abre el fichero csv
        reader = csv.reader(fichero, delimiter=';')   #lee el fichero csv
        for dni, nombre, apellido in reader:      #recorre el fichero csv
            cliente = Cliente(dni, nombre, apellido)      #crea un objeto cliente con los datos del fichero csv
            lista.append(cliente)           #añade el objeto cliente a la lista

    @staticmethod     #método estático para buscar un cliente por su dni
    def buscar(dni):    #funcion para buscar un cliente por su dni
        for cliente in Clientes.lista:      #recorre la lista de clientes
            if cliente.dni == dni:    #si el dni del cliente es igual al dni pasado por parámetro devuelve el cliente
                return cliente

    @staticmethod
    def crear(dni, nombre, apellido):    #funcion para crear un cliente
        cliente = Cliente(dni, nombre, apellido)     #crea un objeto cliente con los datos pasados por parámetro
        Clientes.lista.append(cliente)      #añade el objeto cliente a la lista
        Clientes.guardar()    #guarda los datos en el fichero csv
        return cliente     #devuelve el cliente

    @staticmethod
    def modificar(dni, nombre, apellido):    #funcion para modificar un cliente
        for indice, cliente in enumerate(Clientes.lista):    #recorre la lista de clientes
            if cliente.dni == dni:    #si el dni del cliente es igual al dni pasado por parámetro modifica los datos del cliente y devuelve el cliente modificado
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido = apellido
                Clientes.guardar()
                return Clientes.lista[indice]

    @staticmethod
    def borrar(dni):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                cliente = Clientes.lista.pop(indice)
                Clientes.guardar()
                return cliente

    @staticmethod
    def guardar():     #funcion para guardar los datos en el fichero csv
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for cliente in Clientes.lista:
                writer.writerow((cliente.dni, cliente.nombre, cliente.apellido))
    
    