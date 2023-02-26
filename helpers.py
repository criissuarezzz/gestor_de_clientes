import os
import platform
import re

def limpiar_pantalla():      # Función para limpiar la pantalla
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


#Función para leer un texto, que utilizaremos para los campos de dni nombre y apellido
def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):    #longitud minima y maxima del texto, y mensaje opcional
    print(mensaje) if mensaje else None #si mensaje es None, no se imprime nada, si no, se imprime el mensaje
    while True:   
        texto=input("Introduzca un texto: ")  #leemos el texto
        if len(texto) >= longitud_min and len(texto) <= longitud_max:   #comprobamos que el texto cumple las condiciones y si es asi lo devolvemos
            return texto

def dni_valido(dni, lista):     #comprobamos que el dni cumple el formato y que no se repite
    if not re.match('[0-9]{2}[A-Z]$', dni):    #comprobamos que el dni cumple el formato de 2 numeros y 1 letra
        print("DNI incorrecto, debe cumplir el formato.")  #si no cumple el formato, mostramos un mensaje y devolvemos False
        return False
    for cliente in lista:   #recorremos la lista de clientes
        if cliente.dni == dni:  #comprobamos si el dni del cliente coincide con el dni que queremos comprobar 
            print("DNI utilizado por otro cliente.")   #si coincide, mostramos un mensaje y devolvemos False
            return False
    return True