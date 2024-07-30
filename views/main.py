import sys
sys.path.append('../')

from controls.tda.linked.linkedList import Linked_List
from controls.tda.graph.graphLabelManaged import GraphLabelManaged
from controls.tda.graph.graphNoManaged import GraphNoManaged
import random
import time
from controls.historialDaoControl import HistorialDaoControl
import os
from models.sinteticaGrafo import SinteticaGrafo
from controls.sinteticaDaoControl import SinteticaDaoControl
sin = SinteticaDaoControl()
try:
    """sin._sintetica._id
    sin._sintetica._nombre = "Eberson Daniel"
    sin._sintetica._direccion = "Loja"
    sin._sintetica._telefono = "123456"
    sin._sintetica._horario = "8:00 - 18:00"
    sin.save
    sin._sintetica = None

    
    sin._sintetica._id
    sin._sintetica._nombre = "Eberson Danjjjiel"
    sin._sintetica._direccion = "Loja"
    sin._sintetica._telefono = "123456"
    sin._sintetica._horario = "8:00 - 18:00"
    sin.save
    sin._sintetica = None"""
    start_time = time.time() 
    grafo = GraphNoManaged(15) #aumentar 1 para ver el error
    grafo.insert_edges_weight(1,9,5700)
    grafo.insert_edges_weight(1,2,1940)
    grafo.insert_edges_weight(1,3,2240)
    grafo.insert_edges_weight(1,8,1190)
    grafo.insert_edges_weight(1,5,3896950)
    grafo.insert_edges_weight(1,4,45700)
    grafo.insert_edges_weight(1,4,1250)
    grafo.insert_edges_weight(3,4,2323)
    grafo.insert_edges_weight(3,2,9090)
    ht = SinteticaGrafo()
    ht.creat_graph()
    #print('Algoritmo de Dijkstra:')
    print('Algoritmo de Floyd:')
    path, distance = ht.find_shortest_path(14, 11, 2) #1 D, 2 F
    print(f"Camino más corto: {path}, Distancia: {distance} km")
    end_time = time.time()  # Fin del tiempo de medición
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")
    

    
except Exception as e:
    print(f"Error: {e}")