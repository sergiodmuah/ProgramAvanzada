class Publicacion:
    def __init__(self, titulo, autor, anio):
        self._titulo = titulo
        self._autor = autor
        self._anio = anio

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not valor:
            raise ValueError("El título no puede estar vacío.")
        self._titulo = valor

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, valor):
        if not valor:
            raise ValueError("El autor no puede estar vacío.")
        self._autor = valor

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El año debe ser un número entero positivo.")
        self._anio = valor

    def descripcion(self):
        return f"Título: {self._titulo}, Autor: {self._autor}, Año: {self._anio}"

class Libro(Publicacion):
    def __init__(self, titulo, autor, anio, genero):
        super().__init__(titulo, autor, anio)
        self._genero = genero

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, valor):
        if not valor:
            raise ValueError("El género no puede estar vacío.")
        self._genero = valor

    def descripcion(self):
        return f"Libro - {super().descripcion()}, Género: {self._genero}"

class Revista(Publicacion):
    def __init__(self, titulo, autor, anio, num_edicion):
        super().__init__(titulo, autor, anio)
        self._num_edicion = num_edicion

    @property
    def num_edicion(self):
        return self._num_edicion

    @num_edicion.setter
    def num_edicion(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El número de edición debe ser un número entero positivo.")
        self._num_edicion = valor

    def descripcion(self):
        return f"Revista - {super().descripcion()}, Número de edición: {self._num_edicion}"
