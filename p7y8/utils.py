import os
import pickle
from excepciones import ErrorArchivo

def validar_input_tipo(tipo, mensaje):
    """Función para validar el tipo de una entrada de usuario."""
    while True:
        try:
            valor = input(mensaje)
            if tipo == 'int':
                return int(valor)
            elif tipo == 'str':
                return str(valor)
        except ValueError:
            print(f"Por favor, ingrese un valor de tipo {tipo} válido.")

def guardar_publicaciones(publicaciones, nombre_fichero):
    """Guarda las publicaciones en un fichero binario."""
    try:
        with open(nombre_fichero, 'wb') as archivo:
            pickle.dump(publicaciones, archivo)
    except Exception as e:
        raise ErrorArchivo(f"Error al guardar las publicaciones: {e}")

def cargar_publicaciones(nombre_fichero):
    """Carga las publicaciones desde un fichero binario."""
    try:
        with open(nombre_fichero, 'rb') as archivo:
            return pickle.load(archivo)
    except FileNotFoundError:
        raise ErrorArchivo("El archivo no fue encontrado.")
    except Exception as e:
        raise ErrorArchivo(f"Error al cargar las publicaciones: {e}")

def leer_cadena(mensaje):
    while True:
        cadena = input(mensaje).strip()
        if cadena:
            return cadena
        print("Por favor, ingrese una cadena no vacía.")

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
