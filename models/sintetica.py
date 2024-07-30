class Sintetica():
    def __init__(self) -> None:
        self.__id = 0
        self.__nombre = ""
        self.__direccion = ""
        self.__telefono = ""
        self.__latitud = '0.0'
        self.__longitud = '0.0'
        self.__horario = ""

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        self.__telefono = value

    @property
    def _latitud(self):
        return self.__latitud

    @_latitud.setter
    def _latitud(self, value):
        self.__latitud = value

    @property
    def _longitud(self):
        return self.__longitud

    @_longitud.setter
    def _longitud(self, value):
        self.__longitud = value

    @property
    def _horario(self):
        return self.__horario

    @_horario.setter
    def _horario(self, value):
        self.__horario = value

    @property 
    def serialize(self):
        return {
            'id': self._id,
            'nombre': self._nombre,
            'direccion': self._direccion,
            'telefono': self._telefono,
            'latitud': self._latitud,
            'longitud': self._longitud,
            'horario': self._horario
        }

    def __str__(self) -> str:
        return f'{self._nombre} {self._direccion} {self._telefono} {self._horario}'

    def deserializar(self, data):
        self._id = data.get('id', 0)
        self._nombre = data.get('nombre', "")
        self._direccion = data.get('direccion', "")
        self._telefono = data.get('telefono', "")
        self._latitud = data.get('latitud', '0.0')
        self._longitud = data.get('longitud', '0.0')
        self._horario = data.get('horario', "")
        return self
