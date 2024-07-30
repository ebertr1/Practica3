from controls.tda.graph.graphLabelManaged import GraphLabelManaged
from controls.exception.arrayPositionException import ArrayPositionException
from math import nan
from controls.tda.graph.adjacent import Adjacent

class GraphLabelNoManaged(GraphLabelManaged):
    def __init__(self, num_vert, model):        #quitar model
        super().__init__(num_vert, model)

    def insert_edges_weight_L(self, label, label2, weight):
        print(type(label), type(label2), type(self.num_vertex))   
        if not self.exist_Edge_L(label, label2):
                edg = self.num_edges + 1
                self.setNumEdg(edg)
                adj = Adjacent()
                adj._destination = label2
                adj._weight = weight

                adj1 = Adjacent()
                adj1._destination = label
                adj1._weight = weight
                aux = self.adjacent_L(label)
                aux1 = self.adjacent_L(label)
                aux.add(adj, aux._length)
                aux1.add(adj1, aux1._length)
        else:
                raise ArrayPositionException("Delimited out Position out of range")
        
    def insert_edges_L(self, label, label2):
        self.insert_edges_weight_L(label, label2, nan)