from collections import deque

def encontrar_area_maxima(A, B, mapa):
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visitados = [[False for _ in range(B)] for _ in range(A)]
    area_maxima = 0

    for i in range(A):
        for j in range(B):
            if mapa[i][j] == 'X' and not visitados[i][j]:
                cola = deque([(i, j)])
                visitados[i][j] = True
                area_actual = 0

                while cola:
                    x, y = cola.popleft()
                    area_actual += 1
                    for dx, dy in direcciones:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < A and 0 <= ny < B:
                            if mapa[nx][ny] == 'X' and not visitados[nx][ny]:
                                visitados[nx][ny] = True
                                cola.append((nx, ny))
                if area_actual > area_maxima:
                    area_maxima = area_actual

    return area_maxima

C = int(input())
for _ in range(C):
    A, B = map(int, input().split())
    mapa = [input().strip() for _ in range(A)]
    area_maxima = encontrar_area_maxima(A, B, mapa)
    print(area_maxima)