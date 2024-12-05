# c = int(input())
# for _ in range(c):
#     pesos = list(map(int, input().split(", ")))
#     pesos.sort()
#     n = len(pesos) 
#     medio = n // 2
#     fila_izq = pesos[:medio]
#     fila_der = pesos[medio:]
#     diferencia = abs(sum(fila_izq) - sum(fila_der))
#     print(diferencia)

c = int(input())  
for _ in range(c):
    pesos = list(map(int, input().split(", ")))
    pesos.sort() 
    fila_izq = []
    fila_der = [pesos.pop()] 
    for peso in pesos:
        if sum(fila_izq) <= sum(fila_der):
            fila_izq.append(peso) 
        else:
            fila_der.append(peso)  
    if max(fila_izq) >= min(fila_der):
        fila_der.append(fila_izq.pop(fila_izq.index(max(fila_izq))))  
    diferencia = abs(sum(fila_izq) - sum(fila_der))
    print(diferencia)