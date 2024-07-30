from controls.tda.linked.node import Node
from controls.exception.linkedListExeption import LinkedEmptyException
from controls.exception.arrayPositionException import ArrayPositionException
from numbers import Number
from controls.tda.linked.order.burbuja import Burbuja
from controls.tda.linked.order.insersion import Insersion
from controls.tda.linked.order.seleccion import Seleccion
from controls.tda.linked.order.quickSort import QuickSort
from controls.tda.linked.order.mergeSort import MergeSort
from controls.tda.linked.search.binary import Binary
from controls.tda.linked.order.shellSort import ShellSort
from controls.tda.linked.search.binarySecuencial import BinarySecuencial

#from controls.tda.linked.search.binarySecuencial import BinarySecuencial

class Linked_List(object):
    def __init__(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    def __iter__(self):
        node = self._head  # assuming 'head' is the name of the attribute pointing to the first node
        while node is not None:
            yield node._data  # assuming 'data' is the name of the attribute storing node data
            node = node._next  # assuming 'next' is the name of the attribute pointing to the next node

    @property
    def _head(self):
        return self.__head

    @_head.setter
    def _head(self, value):
        self.__head = value

    @property
    def _length(self):
        return self.__length

    @_length.setter
    def _length(self, value):
        self.__length = value

    @property
    def isEmpty(self):
        return self.__head == None or self.__length == 0

    def __addFirst__(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node
            self.__last = node            
        else:
            headOld = self.__head
            node = Node(data, headOld)
            self.__head = node
        
        self.__length += 1

    def __addLast__(self, data):
        if self.isEmpty:
            self.__addFirst__(data)            
        else:            
            node = Node(data)
            self.__last._next = node
            self.__last = node        
            self.__length += 1

    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    def add(self, data, pos = 0):
        if pos == 0:
            self.__addFirst__(data)
        elif pos == self.__length:            
            self.__addLast__(data)
        else:            
            node_preview = self.getNode(pos-1)
            node_last = node_preview._next#self.getNode(pos) 
            node = Node(data, node_last)
            node_preview._next = node
            self.__length += 1
    
    def edit(self, data, pos = 0):
        if pos == 0:
            self.__head._data = data
        elif pos == self.__length:            
            self.__last._data = data
        else:                        
            node = self.getNode(pos)            
            node._data = data
            
    
    def deleteFirst(self):
        if self.isEmpty:
            raise LinkedEmptyException("List empty")
        else:
            element = self.__head._data
            aux = self.__head._next
            self.__head = aux
            if self.__length == 1:
                self.__last = None
            self._length = self._length - 1
            return element
        
    def deleteLast(self):
        if self.isEmpty:
            raise LinkedEmptyException("List empty")
        else:
            element = self.__last._data
            aux = self.getNode(self._length - 2)
            if aux == None:
                self.__last = None
                if self.__length == 2:
                    self.__last = self.__head
                else:
                    self.__head = None
            else:
                self.__last = None
                self.__last = aux
                self.__last._next = None
            self._length = self._length - 1
            return element

    
    def delete(self, pos = 0):
        if self.isEmpty:
            raise LinkedEmptyException("List empty")
        elif pos < 0 or pos >= self.__length:
            raise ArrayPositionException("Position out range")
        elif pos == 0:
            return self.deleteFirst()
        elif pos == (self.__length - 1):
            return self.deleteLast()
        else:
            preview = self.getNode(pos - 1)
            actually = self.getNode(pos)
            element = preview._data
            next = actually._next
            actually = None
            preview._next = next
            self._length = self._length - 1
            return element
    
    def detele(self, pos):
        pos = pos 
        if self.isEmpty:
            raise LinkedEmptyException("List is Empty")
        elif pos < 0 or pos >= self._length:
            raise ArrayPositionException("Position is out of range")
        elif pos == 0:
            self._head = self.__head._next
            self.__length -= 1
            
        elif pos == self._length -1:
            self.__last = self.getNode(pos-1)
            #restarId
            self.__length -= 1
        else:
            node_preview = self.getNode(pos-1)
            node_last = node_preview._next._next
            node_preview._next = node_last
            self.__length -= 1
            
        for i in range(pos, self._length):
            self.getNode(i)._data._id = i+1


    def get(self, index):
        if index < 0 or index >= self._length():
            raise IndexError("Index out of bounds")
        current_index = 0
        for node_data in self:
            if current_index == index:
                return node_data
            current_index += 1

    """Obtiene el objeto nodo"""
    def getNode(self, pos):
        if self.isEmpty:
            raise LinkedEmptyException("List empty")
        elif pos < 0 or pos >= self._length:
            raise ArrayPositionException("Index out range")
        elif pos == 0:
            return self.__head
        elif pos == (self.__length - 1):
            return self.__last
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node
        

    def get(self, pos):
        try:
            return self.getNode(pos)._data
        except Exception as error:
            return None


    def __str__(self) -> str:
        out = ""
        if self.isEmpty:
            out = "List is Empty"
        else:
            node = self.__head
            while node != None:
                out += str(node._data)+ "\t"
                node = node._next
        return out
    
    @property
    def print(self):
        node = self.__head
        data = ""    
        while node != None:
            data += str(node._data)+"    " 
            node = node._next
        print("Lista de datos")
        print(data)

    @property
    def toArray(self):
        array = []
        if not self.isEmpty:
            node = self.__head
            cont = 0
            while cont < self._length:
                array.append(node._data)
                cont += 1
                node = node._next
        return array
    
    def toList(self, array):
        self.clear
        for i in range(0, len(array)):
            self.__addLast__(array[i])

    def sort(self, type, typeSort = 1):
        if self.isEmpty:
            raise LinkedEmptyException("List empty")
        else:
            array = self.toArray
            #solo datos primitivos
            if isinstance(array[0], Number) or isinstance(array[0], str):
                if typeSort == 1:
                    #order = Burbuja()
                    #order = Insersion()
                    #order = Seleccion()
                    order = QuickSort()
                elif typeSort == 2:
                    order = MergeSort()
                else:
                    order = ShellSort()
                if type == 1:
                    #array = order.sort_burbuja_number_ascendent(array)
                    array = order.sort_primitive_ascendent(array)
                else:
                    #array = order.sort_burbuja_number_descendent(array)
                    array = order.sort_primitive_descendent(array)
            self.toList(array)

    def sort_models(self, attribute, type = 1, typeSort = 1):
            if self.isEmpty:
                raise LinkedEmptyException("List empty")
            else:
                array = self.toArray
                if isinstance(array[0], object):
                    if typeSort == 1:
                    #order = Burbuja()
                    #order = Insersion()
                    #order = Seleccion()
                        order = QuickSort()
                    elif typeSort == 2:
                        order = MergeSort()
                    else:
                        order = ShellSort()
                    if type == 1:
                        #array = order.sort_burbuja_attribute_ascendent(array, attribute)
                        array = order.sort_models_ascendent(array, attribute)
                    else:
                        #array = order.sort_burbuja_attribute_descendent(array, attribute)
                        array = order.sort_models_descendent(array, attribute)
                    #cls = getattr(array[0], '_apellidos')
                    #print(cls)
                self.toList(array)
            return self
    
    def search_equals(self, data):
        list = Linked_List()
        if self.isEmpty:
            raise LinkedEmptyException("List empty")
        else:
            array = self.toArray
            for i in range(0, len(array)):
                #if array[i] == data: #comparar numeros o datos, puede ser < o > tambien
                if array[i].lower().endswith(data.lower()): #palabra que termina con data
                #if array[i].lower().startswith(data.lower()): #palabra que comienza con data
                #if array[i].lower().__contains__(data.lower()): #palabra que contiene data
                    list.add(array[i], list._length)
        return list
    
    def binary_search(self, data, type = 1):
        array = self.toArray
        order = QuickSort()
        array = order.sort_primitive_ascendent(array)
        #print(array)
        #print(len(array))
        if self.isEmpty:
            raise LinkedEmptyException("List empty")
        else:
            search = Binary()
            if type == 0:
                return search.binary_string(array, data, 0, len(array) - 1)
            elif type == 1:
                return search.binary_primitive(array, data, 0, len(array) - 1)  
            
    
            
    def binary_search_secuencial(self, data, type = 1):
        array = self.toArray
        order = QuickSort()
        array = order.sort_primitive_ascendent(array)
        if self.isEmpty:
            raise LinkedEmptyException("List empty")
        else:
            search = BinarySecuencial()
            if type == 1:
                #array = search.binary_primitive_secuencial(array, data, 0, len(array) - 1)
                #print(array)
                return search.binary_primitive_secuencial(array, data, 0, len(array) - 1) 
            #elif type == 2:
                #return search.binary_primitive_secuencial(array, data)
                
    def binary_search_models(self, data, attribute, type = 1):
        array = self.toArray
        #order = QuickSort()
        order = ShellSort()
        array = order.sort_models_ascendent(array, attribute)
        if self.isEmpty:
            raise LinkedEmptyException("List empty")
        else:
            search = Binary()
            if type == 1:
                return search.search_binary_models(array, data, attribute, 0, len(array) - 1)
                #self.toList((arraySort))
            elif type == 2:
                return search.search_binary_models_string(array, data, attribute, 0, len(array) - 1)
        
        #return self

            
    def binary_models(self, data, attribute, type = 1):
        array = self.toArray
        order = QuickSort()
        array = order.sort_models_ascendent(array, attribute)
        if self.isEmpty:
            raise LinkedEmptyException("List empty")
        else:
            search = BinarySecuencial()
            if type == 1:
                arraySort = search.binary_models_secuencial(array, data, 0, len(array)-1, attribute)
                self.toList((arraySort))
            return self
            #elif type == 2:
                #return search.binary_models_string(array, data, 0, len(array) - 1, attribute)