from controls.tda.graph.graph import Graph
from controls.tda.linked.linkedList import Linked_List
from controls.exception.arrayPositionException import ArrayPositionException
from controls.tda.graph.adjacent import Adjacent
from controls.tda.graph.algoGrafos.dijkstraDato import DijkstraDato
from controls.tda.graph.algoGrafos.floydDato import FloyDato
from math import nan
class GraphManaged(Graph):
    def __init__(self, num_vert):
        super().__init__()
        self.__numVert = num_vert
        self.__numEdg = 0
        self.__listAdjacent = []
       
        for i in range(0, num_vert+1):
            self.__listAdjacent.append(Linked_List())

    def setNumEdg(self, number):
        self.__numEdg = number
    
    @property
    def num_vertex(self):
        return self.__numVert
    
    @property
    def num_edges(self):
        return self.__numEdg
    
    def get_edge(self, v1, v2):
        if v1 <= self.num_vertex and v2 <= self.num_vertex:
            listAdj = self.__listAdjacent[v1]
            if not listAdj.isEmpty:
                arrayAdj = listAdj.toArray
                for i in range(listAdj._length):
                    adj = arrayAdj[i]
                    if adj._destination == v2:
                        return adj
        else:
            raise ArrayPositionException("Position out of range")
        return None
        
    def exist_edges(self, v1, v2):
        return self.get_edge(v1, v2) is not None
    
    def weight_edges(self, v1, v2):
        edge = self._get_edge(v1, v2)
        if edge:
            return edge._weight
        return None
    
    def insert_edges_weight(self, v1, v2, weight):
        if v1 <= self.num_vertex and v2 <= self.num_vertex:
            if not self.exist_edges(v1, v2):
                self.__numEdg += 1
                adj = Adjacent()
                adj._destination = v2
                adj._weight = weight
                self.__listAdjacent[v1].add(adj, self.__listAdjacent[v1]._length)
        else:
            raise ArrayPositionException("Delimited out Position out of range")
        
    def insert_edges(self, v1, v2):
        self.insert_edges_weight(v1, v2, nan)

    def adjacent(self, v1):
        return self.__listAdjacent[v1]
    
    def find_shortest_path_unlabeled(self, origen, destino, algoritmo=1):
        if algoritmo == 1:
            pesos, error = self.convert_to_weight_matrix_unlabeled()
            if error == 1:
                raise Exception('No se encuentran conectados todos los vertices')
            dijkstra = DijkstraDato(pesos, origen)
            dijkstra.caminoMinimos()
            path = dijkstra.get_path(destino)
            distance = dijkstra.get_distance(destino)
        else:
            pesos, error = self.convert_to_weight_matrix_unlabeled()
            floyd = FloyDato(pesos)
            floyd.calculate_shortest_paths()
            path = floyd.get_path(origen, destino)
            distance = floyd.get_distance(origen, destino)

        return path, distance

    def convert_to_weight_matrix_unlabeled(self):
        matriz = [[float('inf') for _ in range(self.num_vertex)] for _ in range(self.num_vertex)]
        for i in range(self.num_vertex):
            matriz[i][i] = 0
            for adj in self.adjacent(i).toArray:
                matriz[i][adj._destination] = adj._weight
                matriz[adj._destination][i] = adj._weight

        error = None
        for i in range(self.num_vertex):
            if all(matriz[i][j] == float('inf') for j in range(self.num_vertex) if i != j):
                error = 1
                break

        return matriz, error