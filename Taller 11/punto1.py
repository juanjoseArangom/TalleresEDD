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
        
        return distancias

c = int(input())
for caso_num in range(1, c + 1):
    I, B = map(int, input().split(", "))
    grafo = {i: [] for i in range(I)} 

    for _ in range(B):
        persona1, persona2 = map(int, input().split())
        grafo[persona1].append(persona2)
        grafo[persona2].append(persona1)
    distancia_paulina = {i: float('inf') for i in range(I)}  
    distancia_paulina[0] = 0 

    cola = deque([0])  
    while cola:
        persona_actual = cola.popleft()
        for vecino in grafo[persona_actual]:
            if distancia_paulina[vecino] == float('inf'): 
                distancia_paulina[vecino] = distancia_paulina[persona_actual] + 1
                cola.append(vecino)

    print(f"fiesta {caso_num}:")
    for persona in range(1, I):  
        if distancia_paulina[persona] == float('inf'):
            print(f"{persona} INF")
        else:
            print(f"{persona} {distancia_paulina[persona]}")
    if caso_num < c:
        print()