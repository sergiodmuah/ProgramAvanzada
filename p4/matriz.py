import numpy as np

class CMatFloat:
    """
    Clase que representa una matriz dinámica 1D/2D.
    """
    def __init__(self):
        """
        Inicializa la matriz en None y las dimensiones en 0.
        """
        self._Matriz = None
        self._m_nFilas = 0
        self._m_nColumnas = 0

    def CrearMatriz2D(self, nFilas, nColumnas):
        """
        Crea una matriz 2D de ceros.
        """
        self._Matriz = np.zeros((nFilas, nColumnas), dtype=float)
        self._m_nFilas = nFilas
        self._m_nColumnas = nColumnas

    def CrearMatriz1D(self, nElementos):
        """
        Crea una matriz 1D de ceros.
        """
        self.CrearMatriz2D(1, nElementos)

    def Introducir(self):
        """
        Permite al usuario introducir valores para la matriz creada.
        """
        if not self.Existe():
            print("No hay ninguna matriz creada.")
            return

        print("Introduzca los elementos de la matriz:")
        for i in range(self._m_nFilas):
            for j in range(self._m_nColumnas):
                self._Matriz[i, j] = leer_float(f"Elemento [{i}, {j}]: ")

    def Mostrar(self):
        """
        Muestra los elementos de la matriz actual.
        """
        if self.Existe():
            print("Matriz actual:")
            print(self._Matriz)
        else:
            print("No hay ninguna matriz creada.")

    def Existe(self):
        """
        Verifica si la matriz está creada y no está vacía.
        """
        return self._Matriz is not None

    def SumarMatrices(self, otra_matriz):
        """
        Suma la matriz actual con otra matriz.
        """
        if not self.Existe() or not otra_matriz.Existe():
            print("Ambas matrices deben existir para realizar la suma.")
            return None
        if (self._m_nFilas, self._m_nColumnas) != (otra_matriz._m_nFilas, otra_matriz._m_nColumnas):
            print("Las dimensiones de ambas matrices deben coincidir.")
            return None
        return self._Matriz + otra_matriz._Matriz

    def RestarMatrices(self, otra_matriz):
        """
        Resta la matriz actual con otra matriz.
        """
        if not self.Existe() or not otra_matriz.Existe():
            print("Ambas matrices deben existir para realizar la resta.")
            return None
        if (self._m_nFilas, self._m_nColumnas) != (otra_matriz._m_nFilas, otra_matriz._m_nColumnas):
            print("Las dimensiones de ambas matrices deben coincidir.")
            return None
        return self._Matriz - otra_matriz._Matriz


# Funciones auxiliares
def leer_int(mensaje="Introduce un número entero: "):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, introduce un número entero válido.")

def leer_float(mensaje="Introduce un número decimal: "):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, introduce un número decimal válido.")

def crear_menu(opciones_menu):
    print("\n".join([f"{i + 1}. {opcion}" for i, opcion in enumerate(opciones_menu)]))
    return leer_int("Seleccione una opción: ")


# Función principal
def main():
    matriz = CMatFloat()
    opciones_menu = [
        "Construir matriz 1D",
        "Construir matriz 2D",
        "Introducir matriz",
        "Mostrar matriz",
        "Operaciones con matrices",
        "Terminar"
    ]

    while True:
        print("\nMenú Principal:")
        opcion = crear_menu(opciones_menu)

        if opcion == 1:
            nElementos = leer_int("Número de elementos de la matriz 1D: ")
            matriz.CrearMatriz1D(nElementos)
            print("Matriz 1D creada.")
        elif opcion == 2:
            nFilas = leer_int("Número de filas de la matriz 2D: ")
            nColumnas = leer_int("Número de columnas de la matriz 2D: ")
            matriz.CrearMatriz2D(nFilas, nColumnas)
            print("Matriz 2D creada.")
        elif opcion == 3:
            matriz.Introducir()
        elif opcion == 4:
            matriz.Mostrar()
        elif opcion == 5:
            sub_menu_operaciones(matriz)
        elif opcion == 6:
            print("Finalizando el programa.")
            break
        else:
            print("Opción no válida, por favor seleccione una opción correcta.")


def sub_menu_operaciones(matriz):
    opciones_operaciones = [
        "Sumar matrices",
        "Restar matrices",
        "Volver al menú principal"
    ]

    while True:
        print("\nSubmenú de Operaciones con Matrices:")
        opcion = crear_menu(opciones_operaciones)

        if opcion == 1 or opcion == 2:
            otra_matriz = CMatFloat()
            nFilas = matriz._m_nFilas
            nColumnas = matriz._m_nColumnas
            if nFilas == 0 or nColumnas == 0:
                print("No hay una matriz existente para operar.")
                continue

            print("Introduzca los elementos de la segunda matriz:")
            otra_matriz.CrearMatriz2D(nFilas, nColumnas)
            otra_matriz.Introducir()

            if opcion == 1:
                resultado = matriz.SumarMatrices(otra_matriz)
                if resultado is not None:
                    print("Resultado de la suma:")
                    print(resultado)
            elif opcion == 2:
                resultado = matriz.RestarMatrices(otra_matriz)
                if resultado is not None:
                    print("Resultado de la resta:")
                    print(resultado)

        elif opcion == 3:
            break
        else:
            print("Opción no válida, por favor seleccione una opción correcta.")


# Ejecución del programa
if __name__ == "__main__":
    main()
55