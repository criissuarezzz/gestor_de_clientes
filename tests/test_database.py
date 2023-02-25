import copy
import unittest
import csv
import config
import database as db
import helpers

class TestDatabase(unittest.TestCase):
    def setUp(self):  #setUp es un método que se ejecuta antes de cada test
        db.Clientes.lista=[     #se crea una lista de clientes para poder hacer las pruebas
            db.Cliente("15J", "Marta", "Perez"),
            db.Cliente("48H", "Manolo", "Lopez"),
            db.Cliente("28Z", "Ana", "Garcia"), #se crea un cliente no existente
        ]
    def test_buscar_cliente(self):   #se crea un test para comprobar que se puede buscar un cliente
        cliente_existente=db.Clientes.buscar("15J")    #se busca un cliente que existe
        cliente_inexistente=db.Clientes.buscar("99X")   #se busca un cliente que no existe
        self.assertIsNotNone(cliente_existente) #assertIsNotNone comprueba que el objeto no es None, se usa para comprobar que existe
        self.assertIsNone(cliente_inexistente) #assertIsNone comprueba que el objeto es None, se usa para comprobar que no existe
    def test_crear_cliente(self):
        nuevo_cliente=db.Clientes.crear('39X', 'Héctor', 'Costa') #se crea un nuevo cliente
        self.assertEqual(len(db.Clientes.lista), 4) #se comprueba que la lista de clientes tiene 4 elementos
        self.assertEqual(nuevo_cliente.nombre, 'Héctor')   #se comprueba que el nombre del cliente es el que se le ha asignado
        self.assertEqual(nuevo_cliente.apellido, 'Costa') #se comprueba que los apellidos del cliente son los que se le han asignado

    def test_modificar_cliente(self):
        cliente_a_modificar=copy.copy(db.Clientes.buscar("28Z")) #se crea una copia del cliente a modificar
        cliente_modificado=db.Clientes.modificar("28Z", "Mariana", "Garcia") #se modifica el cliente
        self.assertEqual(cliente_a_modificar.nombre, "Ana") #se comprueba que el nombre del cliente a modificar es Juan
        self.assertEqual(cliente_modificado.nombre, "Mariana") #se comprueba que el nombre del cliente modificado es Hector
    
    def test_borrar_cliente(self):
        cliente_borrado= db.Clientes.borrar("48H") #se elimina un cliente
        cliente_rebuscado=db.Clientes.buscar("48H") #se busca el cliente eliminado
        self.assertEqual(cliente_borrado.dni, "48H") #se comprueba que el dni del cliente borrado es el que se le ha asignado
        self.assertIsNone(cliente_rebuscado) #se comprueba que el cliente borrado no existe

    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('00A', db.Clientes.lista))  #se comprueba si un dni es válido
        self.assertFalse(helpers.dni_valido('232323S', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('F35', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('48H', db.Clientes.lista))  
        
    def test_escritura_csv(self):   #se comprueba que se puede escribir en el fichero csv
        db.Clientes.borrar('48H')  #se borra un cliente
        db.Clientes.borrar('15J')   #se borra otro cliente
        db.Clientes.modificar('28Z', 'Mariana', 'García')   #se modifica un cliente

        dni, nombre, apellido = None, None, None    #se inicializan las variables
        with open(config.DATABASE_PATH, newline='\n') as fichero:   #se abre el fichero csv
            reader = csv.reader(fichero, delimiter=';')   #se crea un lector de csv separado por ;
            dni, nombre, apellido = next(reader)  #se leen los datos del primer cliente

        self.assertEqual(dni, '28Z')  #se comprueba que el dni del cliente son los que se esperan
        self.assertEqual(nombre, 'Mariana')    #se comprueba que el nombre del cliente son los que se esperan
        self.assertEqual(apellido, 'García')   #se comprueba que los apellidos del cliente son los que se esperan

    
if __name__ == '__main__':
    unittest.main()    #se ejecuta el test
    