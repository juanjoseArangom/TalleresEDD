n = int(input())
valores = input()
numeros = tuple(map(int, valores.split()))
suma = 0
for i in range(len(numeros)-1, -1, -1):
    suma += numeros[i] 
    if i == len(numeros)-1:
        pass
    else:
        print(suma)
