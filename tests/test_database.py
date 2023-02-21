import copy
import unittest
import csv
import config
import database as db
import helpers

class TestDatabase(unittest.TestCase):
    def setUp(self):  #setUp es un método que se ejecuta antes de cada test
        db.Clientes.lista=[     #se crea una lista de clientes para poder hacer las pruebas
            db.Cliente("15J", "Juan", "Perez"),
            db.Cliente("48H", "Maria", "Gomez"),
            db.Cliente("28Z", "Pedro", "Gonzalez"),
        ]
    def test_buscar_cliente(self):   #se crea un test para comprobar que se puede buscar un cliente
        cliente_existente=db.Clientes.buscar("15J")    #se busca un cliente que existe
        cliente_no_existente=db.Clientes.buscar("15K")   #se busca un cliente que no existe
        self.assertIsNotNone(cliente_existente) #assertIsNotNone comprueba que el objeto no es None, se usa para comprobar que existe
        self.assertIsNone(cliente_no_existente) #assertIsNone comprueba que el objeto es None, se usa para comprobar que no existe
    def test_crear_cliente(self):
        nuevo_cliente=db.Clientes.crear('18H', 'Héctor', 'Lopez') #se crea un nuevo cliente
        self.assertEqual(len(db.Clientes.lista), 4) #se comprueba que la lista de clientes tiene 4 elementos
        self.assertEqual(nuevo_cliente.nombre, 'Héctor')   #se comprueba que el nombre del cliente es el que se le ha asignado
        self.assertEqual(nuevo_cliente.apellido, 'Lopez') #se comprueba que los apellidos del cliente son los que se le han asignado

    def test_modificar_cliente(self):
        cliente_a_modificar=copy.copy(db.Clientes.buscar("15J")) #se crea una copia del cliente a modificar
        cliente_modificado=db.Clientes.modificar("15J", "Hector", "Lopez") #se modifica el cliente
        self.assertEqual(cliente_a_modificar.nombre, "Juan") #se comprueba que el nombre del cliente a modificar es Juan
        self.assertEqual(cliente_modificado.nombre, "Hector") #se comprueba que el nombre del cliente modificado es Hector
    
    def test_eliminar_cliente(self):
        cliente_borrado= db.Clientes.borrar("15J") #se elimina un cliente
        cliente_rebuscado=db.Clientes.buscar("15J") #se busca el cliente eliminado
        self.assertNotEqual(cliente_borrado, cliente_rebuscado) #se comprueba que el cliente borrado no es igual al cliente rebuscado

    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('15J', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('23223S', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('F35', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('48H', db.Clientes.lista))
    
    def test_escritura_csv(self):
        db.Clientes.borrar('48H')
        db.Clientes.borrar('15J')
        db.Clientes.modificar('28Z', 'Mariana', 'García')

        dni, nombre, apellido = None, None, None
        with open(config.DATABASE_PATH, newline='\n') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            dni, nombre, apellido = next(reader)

        self.assertEqual(dni, '28Z')
        self.assertEqual(nombre, 'Mariana')
        self.assertEqual(apellido, 'García')

    
if __name__ == '__main__':
    unittest.main()
    