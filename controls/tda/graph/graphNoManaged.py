from controls.tda.graph.graphManaged import GraphManaged
from controls.tda.graph.adjacent import Adjacent
from controls.exception.arrayPositionException import ArrayPositionException
class GraphNoManaged(GraphManaged):
    def __init__(self, num_vert):
        super().__init__(num_vert)

    def insert_edges_weight(self, v1, v2, weight):
        if v1 <= self.num_vertex and v2 <= self.num_vertex:
            if not self.exist_edges(v1, v2):
                edg = self.num_edges + 1
                self.setNumEdg(edg)
                adj = Adjacent()
                adj._destination = v2
                adj._weight = weight

                adj1 = Adjacent()
                adj1._destination = v1
                adj1._weight = weight
                aux = self.adjacent(v1)
                aux1 = self.adjacent(v2)
                aux.add(adj, aux._length)
                aux1.add(adj1, aux1._length)
        else:
            raise ArrayPositionException("Delimited out Position out of range")