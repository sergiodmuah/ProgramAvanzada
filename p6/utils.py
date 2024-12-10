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
