class Floyd:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)
        self.dist = [[float('inf')] * (self.n + 1) for _ in range(self.n + 1)] #para manejar índices desde 0, eliminar 1f y 1c
        self.next = [[-1] * (self.n + 1) for _ in range(self.n + 1)]
        for i in range(1, self.n + 1):
            for j in range(1, self.n + 1):
                self.dist[i][j] = graph[i-1][j-1]       #arista enre i y j
                if graph[i-1][j-1] != float('inf'):
                    self.next[i][j] = j

    def calculate_shortest_paths(self):
        for k in range(1, self.n + 1):
            for i in range(1, self.n + 1):
                for j in range(1, self.n + 1):
                    if self.dist[i][k] + self.dist[k][j] < self.dist[i][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]
                        self.next[i][j] = self.next[i][k]

    def get_path(self, origen, destino):
        if self.next[origen][destino] == -1:
            return []
        path = [origen]
        while origen != destino:
            origen = self.next[origen][destino]
            if origen == -1:
                return []
            path.append(origen)
        return path

    def get_distance(self, origen, destino):
        return self.dist[origen][destino]