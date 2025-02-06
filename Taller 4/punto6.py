casos = int(input())
for i in range(casos):
    pesos = list(map(int, input().split(", ")))
    pesos.sort() 
    for j in range(1, len(pesos)):
        if abs(sum(pesos[:-j]) - sum(pesos[-j::])) <= abs(sum(pesos[:-j-1]) - sum(pesos[-j-1::])):
            print(abs(sum(pesos[:-j]) - sum(pesos[-j::])))
            break
        else:
            continue
