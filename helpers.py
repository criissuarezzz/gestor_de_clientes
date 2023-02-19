import os
import platform
import re

def limpiar_pantalla():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


#Función para leer un texto, que utilizaremos para los campos de dni nombre y apellido
def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None #si mensaje es None, no se imprime nada, si no, se imprime el mensaje
    while True:
        texto=input("Introduzca un texto: ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto

def dni_valido(dni, lista):
    if not re.match('[0-9]{2} [A-Z]$', dni):
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print("El DNI introducido es de otro cliente")
            return False
    return True
