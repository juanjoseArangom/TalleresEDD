listica = []
turnos = []
while True:
    entrada = input().split()
    if entrada[0] == "0" and entrada[1] == "0":
        break
    else:
        entrada[1] = int(entrada[1])
        turnos.append(entrada[1])
        listica.append(entrada[0])
        i = 0
        while i < len(turnos):
            if turnos[i] <= len(listica):
                listica.pop(i)
                turnos.pop(i)
            else:
                i += 1
print(len(listica))