from models.sintetica import Sintetica
from controls.dao.daoAdapter import DaoAdapter

class SinteticaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Sintetica)
        self.__sintetica = None

    @property
    def _sintetica(self):
        if self.__sintetica is None:
            self.__sintetica = Sintetica()
        return self.__sintetica

    @_sintetica.setter
    def _sintetica(self, value):  
        self.__sintetica = value

    @property
    def _lista(self):
        return self._list

    @property
    def save(self):
        lista = self._lista()
        self._sintetica._id = lista._length + 1
        self._save(self._sintetica)
    
    def merge(self, pos):
        self._merge(self._sintetica, pos)
    
    def delete(self, pos):
        self._delete(self._sintetica, pos)
