class Historial():
    def __init__(self) -> None:
        self.__id = 0
        self.__origin = 0
        self.__destination = 0

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _origin(self):
        return self.__origin

    @_origin.setter
    def _origin(self, value):
        self.__origin = value

    @property
    def _destination(self):
        return self.__destination

    @_destination.setter
    def _destination(self, value):
        self.__destination = value

    @property
    def serialize(self):
        return {
            "id": self._id,
            "origin": self._origin,
            "destination": self._destination
        }
    
    def deserializar(self, data):
        historial = Historial()
        historial._id = data['id']
        historial._origin = data['origin']
        historial._destination = data['destination']
        return historial