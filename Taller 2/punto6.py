c = int(input())

for _ in range(c):
    tamaño = int(input())
    valores = tuple(map(int, input().split()))
    posicion = 0
    contador = 0
    anteriores = []  # Inicializar fuera del bucle for
    while True:
        # Verificar si la posición está fuera de los límites
        if posicion < 0 or posicion >= tamaño:
            break
        # Verificar si ya se visitó la posición actual
        if posicion in anteriores:
            break
        # Registrar la posición actual como visitada
        anteriores.append(posicion)
        # Realizar el salto y actualizar el contador
        posicion += valores[posicion]
        contador += 1
    print(contador)