listica = []
sumita = 0
while True:
    entrada = input().split()
    letra = entrada[0]
    numerin = int(entrada[1]) if len(entrada) > 1 else None
    if letra == "E":
        break
    elif letra == "A": 
        listica.append(numerin)
    else: 
        for num in listica:
            if num % numerin == 0:
                sumita += num
        print(sumita)
        sumita = 0