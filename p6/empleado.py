from ficha import Ficha
class Empleado(Ficha):
    def __init__(self, nombre="", edad=0, nacio=None, categoria="", antiguedad=0):
        super().__init__(nombre, edad, nacio)
        self._categoria = categoria
        self._antiguedad = antiguedad

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        self._categoria = value

    @property
    def antiguedad(self):
        return self._antiguedad

    @antiguedad.setter
    def antiguedad(self, value):
        self._antiguedad = value

    def visualizar(self):
        return f"{super().visualizar()}, Categoría: {self._categoria}, Antigüedad: {self._antiguedad} años"
