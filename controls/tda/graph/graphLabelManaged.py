from controls.tda.graph.graphManaged import GraphManaged
from controls.exception.arrayPositionException import ArrayPositionException
from math import nan
import os


class GraphLabelManaged(GraphManaged):
    def __init__(self, num_vert, models):
        super().__init__(num_vert)
        self.__labels = [model._nombre for model in models] 
        self.__labelsVertex = {model._nombre: i for i, model in enumerate(models)}  
    @property
    def _labels(self):
        return self.__labels

    @_labels.setter
    def _labels(self, value):
        self.__labels = value
    
    def getVertexLabel(self, label):
        try:
            return self.__labelsVertex[str(label)]
        except Exception as error:
            return -1

    def labelVertex(self, v, label):
        self._labels[v] = label
        self.__labelsVertex[str(label)] = v
        #print(self.__labelsVertex)

    def getLabel(self, v):
        return self._labels[v]
    
    def set_label(self, vertex, label):
        if vertex < self.num_vertex:
            self.__labelsVertex[vertex] = label
        else:
            raise ArrayPositionException("Delimite out")
        
    def exist_Edge_L(self, label, label2):
        v = self.getVertexLabel(label)
        v2 = self.getVertexLabel(label2)
        if v != -1 or v2 != -1:
            return self.exist_edges(v, v2)
        else: return False
    
    def insert_edges_weight_L(self, label, label2, weight):
        v = self.getVertexLabel(label)
        v2 = self.getVertexLabel(label2)
        if v != -1 or v2 != -1:
            self.insert_edges_weight(v, v2, weight)
        else:
            raise ArrayPositionException("Insert")
        
    def insert_edges_L(self, label, label2):
        self.insert_edges_weight_L(label, label2, nan)

    def weight_edges_L(self, label, label2):
        v = self.getVertexLabel(label)
        v2 = self.getVertexLabel(label2)
        if v != -1 or v2 != -1:
            return self.weight_edges(v, v2)
        else:
            raise ArrayPositionException("Weight")
        
    def adjacent_L(self, label):
        v = self.getVertexLabel(label)
        if v != -1:
            return self.adjacent(v)
        else:
            raise ArrayPositionException("adjacent")


    def paint_graph(self):
        url = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), "static", "d3", "grafo.js")
        js = 'var nodes = new vis.DataSet(['
        for i in range(self.num_vertex):
            label = self.getLabel(i)
            #print('\nholaa')
            #print(label)
            js += '{id: ' + str(i+1) + ', label: "' + str(label) + '"},' + '\n'
        js += ']);\n'
        js += 'var edges = new vis.DataSet([\n'
       
        
        for i in range(self.num_vertex):
            init = str(i+1)
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(adjs._length):
                    adj = adjs.get(j)
                    if isinstance(adj._destination, int):
                        destination_label = self.getLabel(adj._destination)
                    else:
                        destination_label = adj._destination
                    des = str(self.__labels.index(destination_label) + 1)
                    js += '{from: ' + init + ', to: ' + des + ', label: "' + str(adj._weight) +' km' '"},' + '\n' #quitar km para que no salga en el grafo
        js += ']);\n'
       
        js += 'var container = document.getElementById("mynetwork");\n'
        js += 'var data = {nodes: nodes, edges: edges};\n'
        js += 'var options = {};\n'
        js += 'var network = new vis.Network(container, data, options);'
        
        
        with open(url, "w") as a:
            a.write(js)
        