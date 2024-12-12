n, t = list(map(int, input().split()))
listica = []
for i in range(1, n + 1):
    r, k = list(map(int, input().split()))
    if n - k >= 0:
        t -= k
    if i % 5 != 0:
        listica.append((r, k))
if len(listica) > 0 and t > 0:
    contador = 1
    while True:
        if len(listica) > 0:
            if t - listica[0][1] >= 0:
                t -= listica[0][1]
                contador += 1
            else:
                print(listica[0][0], t)
                break
            if contador % 5 == 0:
                listica.pop(0)
            else:
                listica.append(listica.pop(0))
        else:
            print("quedaron boletas disponibles")
            break

