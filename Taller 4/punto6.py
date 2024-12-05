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


casos = int(input())
for i in range(casos):
    pesos = list(map(int, input().split(", ")))
    pesos.sort() 
    for j in range(1, len(pesos)):
        print(pesos[:-j], pesos[-j::], abs(sum(pesos[:-j]) - sum(pesos[-j::])))
        print(pesos[:-j-1], pesos[-j-1::], abs(sum(pesos[:-j-1]) - sum(pesos[-j-1::])))
        if abs(sum(pesos[:-j]) - sum(pesos[-j::])) <= abs(sum(pesos[:-j-1]) - sum(pesos[-j-1::])):
            print(abs(sum(pesos[:-j]) - sum(pesos[-j::])))
            break
        else:
            continue
