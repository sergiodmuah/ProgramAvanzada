from cliente import Cliente
from empleado import Empleado
class RegistroDiario:
    def __init__(self):
        self._personas = []

    def agregar_persona(self, persona):
        if isinstance(persona, (Empleado, Cliente)):
            self._personas.append(persona)
        else:
            raise ValueError("Solo se pueden agregar objetos de tipo Empleado o Cliente.")

    def visualizar_registro(self):
        return [persona.visualizar() for persona in self._personas]

    def visualizar_empleados(self):
        return [persona.visualizar() for persona in self._personas if isinstance(persona, Empleado)]

    def es_empleado(self, persona):
        return isinstance(persona, Empleado)

    def __getitem__(self, index):
        if 0 <= index < len(self._personas):
            return self._personas[index].visualizar()
        raise IndexError("Índice fuera de rango.")

    def __add__(self, otro_registro):
        nuevo_registro = RegistroDiario()
        nuevo_registro._personas = self._personas + otro_registro._personas
        return nuevo_registro
