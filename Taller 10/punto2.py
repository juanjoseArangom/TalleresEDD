N, T = map(int, input().split())
arreglo = [int(input()) for _ in range(N)]
arreglo.sort()
ternas = set()

dic = {valor: indice for indice, valor in enumerate(arreglo)}

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        Ak = T - (arreglo[i] + arreglo[j])
        if Ak in dic and dic[Ak] > j:
            ternas.add((arreglo[i], arreglo[j], Ak))

if not ternas:
    print("No hay trillizas")
else:
    for terna in sorted(ternas):
        print(terna[0], terna[1], terna[2])