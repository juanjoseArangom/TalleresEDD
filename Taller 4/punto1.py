from bisect import bisect_left, bisect, bisect_right
n = int(input())
listica = tuple(map(int, input().split()))
c = int(input())
suma = 0
m = tuple(map(int, input().split()))
for i in m:
    indice = bisect_left(listica, i)
    if indice < len(listica) and listica[indice] == i:
        suma += indice + 1
print(suma)