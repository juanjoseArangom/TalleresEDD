c = int(input())
for _ in range(c):
    cambios = 0
    documentos = list(map(int, input().split()))
    n = len(documentos)
    for _ in range(n):
        for i in range(len(documentos) - 1):
            if documentos[i] > documentos[i + 1]:
                cambios += 1
                documentos[i], documentos[i + 1] = documentos[i + 1], documentos[i]
    print(cambios)