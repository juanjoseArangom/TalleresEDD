from bisect import bisect_left
k = int(input())
lamparas = list(map(int, input().split()))
lamparas.sort()
p = int(input())
for _ in range(p):
    distancia = 0
    uno, dos = map(int, input().split())
    uno = bisect_left(lamparas, uno)
    dos = bisect_left(lamparas, dos)
    distancia = ((uno - dos) ** 2) ** 0.5
    print(int(distancia), "kms")
    