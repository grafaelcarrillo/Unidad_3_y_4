class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def añadir_arista(self, u, v, w):
        self.graph.append([u, v, w])

    def encontrar(self, parent, i):
        if parent[i] == i:
            return i
        return self.encontrar(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_raiz = self.encontrar(parent, x)
        y_raiz = self.encontrar(parent, y)

        if rank[x_raiz] < rank[y_raiz]:
            parent[x_raiz] = y_raiz
        elif rank[x_raiz] > rank[y_raiz]:
            parent[y_raiz] = x_raiz
        else:
            parent[y_raiz] = x_raiz
            rank[x_raiz] += 1

    def algoritmo_kruskal(self):
        resultado = []
        i, e = 0, 0

        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.encontrar(parent, u)
            y = self.encontrar(parent, v)

            if x != y:
                e += 1
                resultado.append([u, v, w])
                self.union(parent, rank, x, y)

        return resultado

g = Graph(4)
g.añadir_arista(0, 1, 10)
g.añadir_arista(0, 2, 6)
g.añadir_arista(0, 3, 5)
g.añadir_arista(1, 3, 15)
g.añadir_arista(2, 3, 4)

result = g.algoritmo_kruskal()
print("Aristas en el árbol de expansión mínima:")
for u, v, w in result:
    print(f"{u} -- {v}  peso: {w}")
