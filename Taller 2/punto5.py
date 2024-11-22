c = int(input())
for _ in range(c):
    M, N = map(int, input().split())
    monedas = tuple(map(int, input().split()))
    acumulados = (0,) * M
    for i, moneda in enumerate(monedas):
        acumulados = tuple(
            acumulados[j] + moneda if j == (i % M) else acumulados[j]
            for j in range(M)
        )
    diferencia = max(acumulados) - min(acumulados)
    print(diferencia)