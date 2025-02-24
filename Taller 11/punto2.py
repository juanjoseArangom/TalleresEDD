from collections import deque

class Grafo:
    def __init__(self, nodos):
        self.nodos = nodos
        self.adj = {i: [] for i in range(nodos)}
    
    def agregar_arista(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    
    def bfs(self, inicio):
        distancias = {i: float('inf') for i in range(self.nodos)}
        distancias[inicio] = 0 
        cola = deque([inicio])
        
        while cola:
            nodo_actual = cola.popleft()
            for vecino in self.adj[nodo_actual]:
                if distancias[vecino] == float('inf'):
                    distancias[vecino] = distancias[nodo_actual] + 1 
                    cola.append(vecino)
        conteo_dias = {}
        for dia in distancias.items():
            if dia != float('inf') and dia != 0:  
                conteo_dias[dia] = conteo_dias.get(dia, 0) + 1

        if not conteo_dias:
            return 0

        radio = max(conteo_dias.values())
        diamax = min(dia for dia, radio in conteo_dias.items() if radio == radio)

        return diamax, radio

p = int(input())
grafo = Grafo(p)

for persona in range(p):
    conocidos = list(map(int, input().split()))
    if conocidos[0] == -1:
        continue
    for conocido in conocidos:
        grafo.agregar_arista(persona, conocido)

pruebas = list(map(int, input().split(", ")))
for i in pruebas:
    resultados = grafo.bfs(i)
    if resultados == 0:
        print(0)
    else:
        print(resultados[0], resultados[1])