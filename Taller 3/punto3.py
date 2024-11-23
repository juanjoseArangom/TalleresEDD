listica = []
while True:
    entrada = input().split()
    if entrada[0] == "end":
        break
    elif len(entrada) == 1 or len(entrada) == 2:
        if entrada[0].isdigit():
            entrada = int(entrada[0])
            listica.append(entrada)
        elif entrada[0] == "C" or (entrada[0] == "D" and entrada[1] == "1"):
            listica = listica[:-1]
        elif entrada[0] == "D" and entrada[1].isdigit():
            if int(entrada[1]) <= len(listica) and int(entrada[1]) >= 0:
                listica = listica[:-int(entrada[1])]
    elif len(entrada) == 3 and entrada[1].isdigit() and entrada[2].isdigit():
        n, m = int(entrada[1]), int(entrada[2])
        if n > len(listica) or m > len(listica):
            pass
        else:
            print(*listica[n-1:m], sep="")

