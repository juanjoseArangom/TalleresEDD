listica = []
while True:
    entrada = input().split()
    if entrada[0] == "0" and entrada[1] == "0":
        break
    identificacion = entrada[0]
    maximo = int(entrada[1])
    listica.append((identificacion, maximo)) 
    while True:
        excede = False
        for i in range(len(listica)):
            if len(listica) > listica[i][1]:
                listica.pop(i)
                excede = True
                break
        if not excede:
            break
print(len(listica))
