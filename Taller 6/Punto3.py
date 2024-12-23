import heapq

c = int(input())
for _ in range(c):
    numeros = list(map(int, input().split()))[:-1]
    heapq.heapify(numeros)
    while len(numeros) > 2:
        menor1 = heapq.heappop(numeros)
        menor2 = heapq.heappop(numeros)
        heapq.heappush(numeros, menor1 + menor2)

    ultimo1 = heapq.heappop(numeros)
    ultimo2 = heapq.heappop(numeros)

    print(ultimo1, ultimo2)
