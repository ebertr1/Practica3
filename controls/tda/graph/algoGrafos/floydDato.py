class FloyDato:
    def __init__(self, pesos):
        self.pesos = pesos
        self.n = len(pesos)
        self.distancias = [[float('inf') for _ in range(self.n)] for _ in range(self.n)]
        self.predecesores = [[None for _ in range(self.n)] for _ in range(self.n)]

    def calculate_shortest_paths(self):
        # Inicializar distancias y predecesores
        for i in range(self.n):
            for j in range(self.n):
                self.distancias[i][j] = self.pesos[i][j]
                if i != j and self.pesos[i][j] < float('inf'):
                    self.predecesores[i][j] = i
                else:
                    self.predecesores[i][j] = None

        # Algoritmo de Floyd-Warshall
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.distancias[i][k] + self.distancias[k][j] < self.distancias[i][j]:
                        self.distancias[i][j] = self.distancias[i][k] + self.distancias[k][j]
                        self.predecesores[i][j] = self.predecesores[k][j]

    def get_path(self, origen, destino):
        if self.predecesores[origen][destino] is None:
            return []
        path = [destino]
        while origen != destino:
            destino = self.predecesores[origen][destino]
            path.insert(0, destino)
        return path

    def get_distance(self, origen, destino):
        return self.distancias[origen][destino]