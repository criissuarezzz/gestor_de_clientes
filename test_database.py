import copy
import unittest
import database as db

class TestDatabase(unittest.TestCase):
    def setUp(self):
        db.Clientes.lista=[
            db.Cliente("15J", "Juan", "Perez"),
            db.Cliente("48H", "Maria", "Gomez"),
            db.Cliente("28Z", "Pedro", "Gonzalez"),
        ]
    def test_buscar_cliente(self):
        cliente_existente=db.Clientes.buscar("15J")
        cliente_no_existente=db.Clientes.buscar("15K")
        self.assertIsNotNone(cliente_existente) #assertIsNotNone comprueba que el objeto no es None, se usa para comprobar que existe
        self.assertIsNone(cliente_no_existente) #assertIsNone comprueba que el objeto es None, se usa para comprobar que no existe
