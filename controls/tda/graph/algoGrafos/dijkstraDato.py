from sys import maxsize

class DijkstraDato:
    def __init__(self, pesos, origen):
        self.n = len(pesos)  # Número de vértices
        self.s = origen  # Origen ya está en base 0
        self.Pesos = pesos
        self.ultimo = [0] * self.n
        self.D = [maxsize] * self.n
        self.F = [False] * self.n

    def caminoMinimos(self):
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
        current = destino  # destino ya está en base 0
        while current != self.s:
            path.insert(0, current)  # No es necesario ajustar para base 1
            current = self.ultimo[current]
        path.insert(0, self.s)  # No es necesario ajustar para base 1
        return path

    def get_distance(self, destino):
        return self.D[destino]  # destino ya está en base 0