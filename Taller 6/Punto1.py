import heapq

turnos = []
while True:
    entrada = input()
    if entrada == "end":
        break
    elif entrada == "sig":
        if len(turnos) == 0:
            continue
        else: 
            ultimo = heapq.heappop(turnos)
    else:
        heapq.heappush(turnos, int(entrada))
print(ultimo)