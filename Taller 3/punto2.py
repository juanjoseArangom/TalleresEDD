c = int(input())
for _ in range(c):
    n, k = map(int, input().split())
    lista = list(range(1, n+1))
    pos = (k-1) % len(lista)
    while len(lista) > 1:
        eliminado = lista.pop(pos)
        if eliminado % len(lista) == 0:
            k = 1
        else: 
            k = (eliminado) % len(lista)
        pos = (pos + k-1) % len(lista)
    print(lista[0])