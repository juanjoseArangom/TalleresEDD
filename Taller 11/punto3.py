# from collections import deque

# class Grafo:
#     def __init__(self, nodos):
#         self.nodos = nodos
#         self.adj = {i: [] for i in range(nodos)}
    
#     def agregar_arista(self, u, v):
#         self.adj[u].append(v)
#         self.adj[v].append(u)
    
#     def bfs(self, inicio, visitados):
#         cola = deque([inicio])
#         visitados.add(inicio)
#         tamano_familia = 0
        
#         while cola:
#             nodo_actual = cola.popleft()
#             tamano_familia += 1
#             for vecino in self.adj[nodo_actual]:
#                 if vecino not in visitados:
#                     visitados.add(vecino)
#                     cola.append(vecino)
        
#         return tamano_familia

# def encontrar_familias(relaciones):
#     nodos = set()
#     for u, v in relaciones:
#         nodos.add(u)
#         nodos.add(v)
#     num = len(nodos)
#     grafo = Grafo(num)
#     for u, v in relaciones:
#         grafo.agregar_arista(u, v)
#     visitados = set()
#     cantidad_familias = 0
#     tamano_maximo = 0
    
#     for nodo in nodos:
#         if nodo not in visitados:
#             tamano_familia = grafo.bfs(nodo, visitados)
#             cantidad_familias += 1
#             if tamano_familia > tamano_maximo:
#                 tamano_maximo = tamano_familia
    
#     return cantidad_familias, tamano_maximo

# C = int(input())
# for _ in range(C):
#     R = int(input())
#     relaciones = []
#     for _ in range(R):
#         u, v = map(int, input().split())
#         relaciones.append((u, v))
    
#     cantidad_familias, tamano_maximo = encontrar_familias(relaciones)
#     print(cantidad_familias, tamano_maximo)

from collections import deque, defaultdict

class Grafo:
    def __init__(self):
        self.adj = defaultdict(list)  
    
    def agregar_arista(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    
    def bfs(self, inicio, visitados):
        cola = deque([inicio])
        visitados.add(inicio)
        tamano_familia = 0
        
        while cola:
            nodo_actual = cola.popleft()
            tamano_familia += 1
            for vecino in self.adj[nodo_actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        
        return tamano_familia

def encontrar_familias(relaciones):
    grafo = Grafo()
    for u, v in relaciones:
        grafo.agregar_arista(u, v)
    visitados = set()
    cantidad_familias = 0
    tamano_maximo = 0
    
    for nodo in grafo.adj:
        if nodo not in visitados:
            tamano_familia = grafo.bfs(nodo, visitados)
            cantidad_familias += 1
            if tamano_familia > tamano_maximo:
                tamano_maximo = tamano_familia
    
    return cantidad_familias, tamano_maximo

C = int(input())
for caso in range(C):
    R = int(input())
    relaciones = []
    for _ in range(R):
        u, v = map(int, input().split())
        relaciones.append((u, v))
    cantidad_familias, tamano_maximo = encontrar_familias(relaciones)
    print(cantidad_familias, tamano_maximo)