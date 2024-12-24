import heapq
 
listica_a = []
listica_b = []
listica_c = []
puntos_a = 0
puntos_b = 0
puntos_c = 0
 
while True:
    entrada = input()
    if entrada == "fin del juego":
        print("Equipo A: ", puntos_a)
        print("Equipo B: ", puntos_b)
        print("Equipo C: ", puntos_c)
        break
    else:
        if entrada != "menores":
            listica = entrada.split()
            equipo, punto = listica[0], int(listica[1])
            if equipo == "A":
                heapq.heappush(listica_a, punto)
            elif equipo == "B":
                heapq.heappush(listica_b, punto)       
            elif equipo == "C":
                heapq.heappush(listica_c, punto)

        else:
            mini_lista = []
            if listica_a:
                punto1 = heapq.heappop(listica_a)
                mini_lista.append((punto1, 'A'))
            if listica_b:
                punto2 = heapq.heappop(listica_b)
                mini_lista.append((punto2, 'B'))
            if listica_c:
                punto3 = heapq.heappop(listica_c)
                mini_lista.append((punto3, 'C'))
            if mini_lista:
                mini_lista.sort()
                menor_punto = mini_lista[0][0]
 
                for punto, equipo in mini_lista:
                    if punto == menor_punto:
                        if equipo == 'A':
                            puntos_a += 1
                        elif equipo == 'B':
                            puntos_b += 1
                        elif equipo == 'C':
                            puntos_c += 1
            else:
                continue



