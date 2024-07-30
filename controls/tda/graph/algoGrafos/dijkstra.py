from sys import maxsize
class Dijkstra:
    def __init__(self, graph, origen):
        self.n = len(graph)  
        self.s = origen - 1 
        self.Pesos = graph
        self.ultimo = [0] * self.n
        self.D = [maxsize] * self.n
        self.F = [False] * self.n

    def minimun_roads(self):
        for i in range(self.n):
            self.D[i] = self.Pesos[self.s][i]
            self.ultimo[i] = self.s
        self.F[self.s] = True
        self.D[self.s] = 0

        for _ in range(1, self.n):
            v = self.minimo()
            self.F[v] = True
            for w in range(self.n):
                if not self.F[w]:
                    if self.D[v] + self.Pesos[v][w] < self.D[w]:
                        self.D[w] = self.D[v] + self.Pesos[v][w]
                        self.ultimo[w] = v

    def minimo(self):
        mx = maxsize
        v = 0
        for j in range(self.n):
            if not self.F[j] and self.D[j] <= mx:
                mx = self.D[j]
                v = j
        return v

    def get_path(self, destino):
        path = []
        current = destino - 1 
        while current != self.s:
            path.insert(0, current + 1) 
            current = self.ultimo[current]
        path.insert(0, self.s + 1)  
        return path

    def get_distance(self, destino):
        return self.D[destino - 1]  