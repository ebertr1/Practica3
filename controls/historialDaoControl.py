from models.historial import Historial  
from controls.dao.daoAdapter import DaoAdapter

class HistorialDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Historial)
        self.__historial = None

    @property
    def _historial(self):
        if self.__historial == None:
            self.__historial = Historial()
        return self.__historial

    @_historial.setter
    def _historial(self, value):
        self.__historial = value

    @property
    def _lista(self):
        return self._list
    
    @property
    def save(self):
        lista = self._lista()
        # Comprobación de existencia de historial con mismo origen y destino
        for historial in lista:
            if (self._historial._origin == historial._origin and self._historial._destination == historial._destination) or \
                (self._historial._origin == historial._destination and self._historial._destination == historial._origin):
                #raise Exception("Ya existe un historial con los mismos valores")
                return False
        self._historial._id = lista._length + 1
        self._save(self._historial)
        #return True
    def merge(self, pos):
        self._merge(self._historial, pos)

    def delete(self, pos):
        self._delete(self._historial, pos)
