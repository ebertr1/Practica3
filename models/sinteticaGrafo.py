from controls.sinteticaDaoControl import SinteticaDaoControl
from math import radians, cos, sin, sqrt, atan2
from controls.tda.graph.graphLabelNoManaged import GraphLabelNoManaged
from controls.historialDaoControl import HistorialDaoControl
from controls.tda.graph.algoGrafos.dijkstra import Dijkstra
from controls.tda.graph.algoGrafos.floyd import Floyd

class SinteticaGrafo():
    def __init__(self) -> None:
        self.__graph = None
        self.__hDao = SinteticaDaoControl()

    def creat_graph(self, origin= None, destination = None):
        his = HistorialDaoControl()
        hisLista = his._lista()
        lista = self.__hDao._list()
        if lista._length > 0:
            self.__graph = GraphLabelNoManaged(lista._length, lista)        #quitar lista
            arr = lista.toArray
            for i in range(len(arr)):
                self.__graph.set_label(i, arr[i])
            self.__graph.paint_graph()
        for entry in hisLista:
            origen_id = entry._origin
            destino_id = entry._destination

            objeto_org = self.__hDao._list().binary_search_models(origen_id, '_id')
            objeto_dest = self.__hDao._list().binary_search_models(destino_id, '_id')
            #print('\n\n')
            if objeto_org is not None and objeto_dest is not None:
                distance = self.calculate_distance(objeto_org, objeto_dest)
                self.__graph.insert_edges_weight(origen_id - 1, destino_id - 1, distance)
                self.__graph.insert_edges_weight(destino_id - 1,  origen_id - 1, distance)
            self.__graph.paint_graph()

    def calculate_distance(self, origen, destino):
        R = 6371.0 #radio de la tierra
        # Convertir coordenadas de grados a radianes
        lat1 = float(origen._latitud)
        lat2 = float(destino._latitud)
        lon1 = float(origen._longitud)
        lon2 = float(destino._longitud)
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        # Distancia total en kilómetros
        distance = round(R * c,2)
        return distance

    def find_shortest_path(self, origen, destino, algoritmo=1):
            if algoritmo == 1:
                pesos, error = self.convert_to_weight_matrix()
                dijkstra = Dijkstra(pesos, origen)
                dijkstra.minimun_roads()
                path = dijkstra.get_path(destino)
                distance = dijkstra.get_distance(destino)
            else:
                pesos, error = self.convert_to_weight_matrix()
                floyd = Floyd(pesos)
                floyd.calculate_shortest_paths()
                path = floyd.get_path(origen, destino)  
                distance = floyd.get_distance(origen, destino)  
    
            path_nombres = []
            for i in path:
                sintetica_obj = self.__hDao._list().binary_search_models(i, '_id')
                if sintetica_obj is not None:
                    path_nombres.append(sintetica_obj._nombre)
                else:
                    path_nombres.append(f"ID {i} no encontrado")
            return path_nombres, distance

    def convert_to_weight_matrix(self):
        ht = self.__hDao  
        sintetica_list = ht._list()
        historial = HistorialDaoControl()._lista()
        matriz = [[float('inf') for _ in range(sintetica_list._length)] for _ in range(sintetica_list._length)]
        for i in range(sintetica_list._length):
            matriz[i][i] = 0

        for hist in historial:
            origen_id = hist._origin
            destino_id = hist._destination
            object_org = ht._list().binary_search_models(origen_id, '_id')
            object_dest = ht._list().binary_search_models(destino_id, '_id')
            if object_org is not None and object_dest is not None:
                distancia = self.calculate_distance(object_org, object_dest)
                matriz[object_org._id-1][object_dest._id-1] = distancia
                matriz[object_dest._id-1][object_org._id-1] = distancia
        error = None
        for i in range(sintetica_list._length):
        #verifica que todos los vertices esten conectads
            if all(matriz[i][j] == float('inf') for j in range(sintetica_list._length) if i != j):
                error = 1
                break
             
        return matriz, error

