c = int(input())
for _ in range(c):
    listica = list(map(int, input().split()))
    listica.sort()
    sumas = []
    suma = 1
    for i in range(len(listica)-1):
        if listica[i] == listica[i+1]:
            suma += 1
        else:
            sumas.append(suma)
            suma = 1
    sumas.append(suma)
    print(" ".join(map(str, sumas)))