# import heapq

# C = int(input())
# for _ in range(C):
#     entrada = input().split()
#     N, A, B = map(int, entrada)
#     print(N, A, B)
#     personas = list(range(1, N + 1))

#     while len(personas) > 1:
#         heap = heapq.heapify(personas)
#         for persona in personas:
#             valor_nuevo = (persona * A) % B
#             heapq.heappop(heap)
#             heapq.heappush(heap, valor_nuevo)

#         # Determinar cuántos eliminar
#         sacar = len(personas) // 2 if len(personas) % 2 == 0 else (len(personas) - 1) // 2

#         # Eliminar los menores valores
#         for _ in range(sacar):
#             heapq.heappop(heap)

#         # Actualizar las personas que quedan
#         personas = [persona for _, persona in heap]

#     # Imprimir el último número restante
#     print(personas[0])


import heapq

C = int(input())
for _ in range(C):
    entrada = input().split()
    N, A, B = map(int, entrada)
    personas = list(range(1, N + 1))

    while len(personas) > 1:
        n = len(personas)  
        for _ in range(n):  
            persona = personas.pop(0)  
            valor_nuevo = (persona * A) % B
            personas.append(valor_nuevo)
        heapq.heapify(personas)

        sacar = len(personas) // 2 if len(personas) % 2 == 0 else (len(personas) - 1) // 2
        for _ in range(sacar):
            heapq.heappop(personas)
    print(personas[0])