n = int(input())
for _ in range(n):
    encriptado = input().replace(" ", "")
    long = len(encriptado)
    tupla = tuple(encriptado)
    paso1 = tuple(reversed(tupla))
    paso2 = tuple(
        paso1[i + 1] if i % 2 == 0 and i + 1 < len(paso1) 
        else paso1[i - 1] if i % 2 != 0  
        else paso1[i]
        for i in range(len(paso1))
    )
    final = "".join(paso2)
    print(final)

