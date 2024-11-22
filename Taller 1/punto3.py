n = int(input())
positivos = 0
negativos = 0
for i in range (0, n):
    numero = int(input())
    if numero > 0:
        positivos += numero
    else:
        negativos += numero
print("positivos " + str(positivos) + ", negativos " + str(negativos))