import heapq

# Diccionarios para almacenar los equipos y sus jugadores como heaps
equipos = {"A": [], "B": [], "C": []}
puntos = {"A": 0, "B": 0, "C": 0}

while True:
    entrada = input().strip()
    if entrada == "fin del juego":
        break
    elif entrada == "menores":
        # Extraer el jugador con el menor número de cada equipo (si hay jugadores)
        menores = []
        for equipo, jugadores in equipos.items():
            if jugadores:  # Si hay jugadores en el equipo
                menores.append((heapq.heappop(jugadores), equipo))
        
        if menores:
            # Ordenar por el número más bajo
            menores.sort()
            # Revisar si hay empate o un claro ganador
            if len(menores) == 1 or menores[0][0] < menores[1][0]:
                # Gana el equipo con el menor número
                ganador = menores[0][1]
                puntos[ganador] += 1
            elif len(menores) > 1 and menores[0][0] == menores[1][0]:
                # Empate, ambos obtienen un punto
                for _, equipo in menores:
                    puntos[equipo] += 1
    else:
        # Entrada de un jugador al equipo
        equipo, numero = entrada.split()
        numero = int(numero)
        heapq.heappush(equipos[equipo], numero)

# Imprimir los resultados finales
print(f"Equipo A: {puntos['A']}")
print(f"Equipo B: {puntos['B']}")
print(f"Equipo C: {puntos['C']}")
