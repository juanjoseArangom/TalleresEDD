from collections import deque

movimientos = [
    (-2, -1), (-1, -2), (1, -2), (2, -1),
    (2, 1), (1, 2), (-1, 2), (-2, 1)
]

def convertir_coordenadas(celda):
    letra = celda[0]
    numero = celda[1]
    fila = 8 - int(numero)  
    columna = ord(letra) - ord('A')
    return fila, columna

def movimientos_minimos(partida, destino):
    fila_partida, col_partida = convertir_coordenadas(partida)
    fila_destino, col_destino = convertir_coordenadas(destino)
    if fila_partida == fila_destino and col_partida == col_destino:
        return 0
    distancias = [[-1 for _ in range(8)] for _ in range(8)]
    distancias[fila_partida][col_partida] = 0
    cola = deque([(fila_partida, col_partida)])
    
    while cola:
        fila_actual, col_actual = cola.popleft()
        for df, dc in movimientos:
            fila_nueva = fila_actual + df
            col_nueva = col_actual + dc           
            if 0 <= fila_nueva < 8 and 0 <= col_nueva < 8:
                if distancias[fila_nueva][col_nueva] == -1:
                    distancias[fila_nueva][col_nueva] = distancias[fila_actual][col_actual] + 1
                    if fila_nueva == fila_destino and col_nueva == col_destino:
                        return distancias[fila_nueva][col_nueva]
                    cola.append((fila_nueva, col_nueva))
    return -1

C = int(input())
for _ in range(C):
    partida, destino = input().split()
    movimientos = movimientos_minimos(partida, destino)
    print(movimientos)