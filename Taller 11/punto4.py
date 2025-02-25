from collections import deque, defaultdict

class Grafo:
    def __init__(self, nodos):
        self.nodos = nodos
        self.adj = defaultdict(list)  
    
    def agregar_arista(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    
    def bipartito(self):
        colores = {}  
        for nodo in range(1, self.nodos + 1):
            if nodo not in colores:
                colores[nodo] = 0 
                cola = deque([nodo])
                
                while cola:
                    actual = cola.popleft()
                    for vecino in self.adj[actual]:
                        if vecino not in colores:
                            colores[vecino] = 1 - colores[actual]
                            cola.append(vecino)
                        elif colores[vecino] == colores[actual]:
                            return False  
        return True

C = int(input())
for _ in range(C):
    N, M = map(int, input().split())
    grafo = Grafo(N)
    for _ in range(M):
        u, v = map(int, input().split(", "))
        grafo.agregar_arista(u, v)
    if grafo.bipartito():
        print("bipartito")
    else:
        print("no bipartito")