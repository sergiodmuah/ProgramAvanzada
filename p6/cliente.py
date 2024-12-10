from ficha import Ficha
class Cliente(Ficha):
    def __init__(self, nombre="", edad=0, nacio=None, dni=""):
        super().__init__(nombre, edad, nacio)
        self._dni = dni

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, value):
        self._dni = value

    def visualizar(self):
        return f"{super().visualizar()}, DNI: {self._dni}"

    def __eq__(self, other):
        return isinstance(other, Cliente) and self.nombre == other.nombre and self.edad == other.edad
