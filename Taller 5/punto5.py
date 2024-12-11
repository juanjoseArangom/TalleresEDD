# c = int(input())
# tiempo = 0
# for _ in range(c):
#     entrada = list(map(int, input().split()))
#     cola = list(map(int, input().split()))
#     while entrada[1] in cola and len(cola) > 0:
#         elemento = cola[0]
#         contador = 1
#         while contador < elemento:  
#             tiempo += 5
#             if cola[0] == elemento:  
#                 contador += 1  
#             cola.append(cola.pop(0))  
#         cola.pop(0)
#     print(tiempo)

c = int(input())  
for _ in range(c):
    entrada = list(map(int, input().split()))
    n, k = entrada[0], entrada[1] - 1  
    cola = list(map(int, input().split()))  
    tiempo = 0  
    while True:
        elemento = cola.pop(0)  
        tiempo += 5  
        if k == 0 and elemento == 1:
            print(tiempo)
            break
        if elemento > 1:
            cola.append(elemento - 1)
        if k == 0:
            k = len(cola) - 1  
        else:
            k -= 1 
