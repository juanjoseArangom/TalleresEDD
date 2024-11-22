# c = int(input())
# for _ in range(c):
#     n, k = map(int, input().split())
#     k -= 1
#     pos = 0
#     lista = list(range(1, n+1))
#     while len(lista) > 1:
#         pos = (pos + k) % len(lista)
#         lista.pop(pos)
#         if k % len(lista) == 0:
#             k = 1
#         else: 
#             k = (k+1) % len(lista)
#     print(lista[0])

c = int(input())  # Número de casos
for _ in range(c):
    n, k = map(int, input().split())
    lista = list(range(1, n + 1))  # Estudiantes numerados del 1 al N
    pos = 0  # Posición inicial
    
    while len(lista) > 1:
        # Calcular la posición del estudiante a eliminar
        pos = (pos + k - 1) % len(lista)
        lista.pop(pos)  # Eliminar al estudiante de la posición calculada
        
        # Actualizar K según las reglas
        k = k % len(lista)
        if k == 0:
            k = 1  # Si K es 0, ajustarlo a 1
    
    print(lista[0])  # El ganador