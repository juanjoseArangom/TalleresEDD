import heapq

C = int(input())
for _ in range(C):
    n = int(input())
    numeros = list(map(int, input().split()))
    heapq.heapify(numeros)
    X, Y = [], []
    while numeros:
        X.append(str(heapq.heappop(numeros)))  
        if numeros:
            Y.append(str(heapq.heappop(numeros)))  
    X = int("".join(X))
    if Y:
        Y = int("".join(Y)) 
    else:
        Y = 0
    resultado = X + Y
    print(resultado)
