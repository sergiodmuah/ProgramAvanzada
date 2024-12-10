from datetime import time

class Ficha:
    def __init__(self, nombre="", edad=0, nacio=None):
        self._nombre = nombre
        self._edad = edad
        self._nacio = nacio if nacio else time(0, 0)  # 12:00:00 AM
        
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        self._edad = value

    @property
    def nacio(self):
        return self._nacio

    @nacio.setter
    def nacio(self, value):
        self._nacio = value

    def visualizar(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Nacido a las: {self._nacio}"
