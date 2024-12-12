# Leer el número de casos
num_casos = int(input().strip())

for _ in range(num_casos):
    # Leer el número de discos
    n = int(input().strip())
    
    movimientos = []  # Lista para guardar los movimientos
    while True:
        movimiento = input().strip()
        if movimiento == "X X":  # Fin del caso actual
            break
        movimientos.append(movimiento)
    
    # Inicializar las torres para el caso actual
    torre_A = list(range(n, 0, -1))  # Discos en orden descendente en la torre A
    torre_B = []
    torre_C = []

    secuencia_invalida = False  # Bandera para detectar secuencia inválida

    # Procesar cada movimiento
    for movimiento in movimientos:
        partes = movimiento.split()
        if len(partes) != 2:  # Validar formato de movimiento
            secuencia_invalida = True
            break

        origen, destino = partes  # Separar la torre origen y destino

        # Seleccionar la pila de origen
        if origen == "A":
            pila_origen = torre_A
        elif origen == "B":
            pila_origen = torre_B
        elif origen == "C":
            pila_origen = torre_C
        else:  # Torre origen inválida
            secuencia_invalida = True
            break

        # Seleccionar la pila de destino
        if destino == "A":
            pila_destino = torre_A
        elif destino == "B":
            pila_destino = torre_B
        elif destino == "C":
            pila_destino = torre_C
        else:  # Torre destino inválida
            secuencia_invalida = True
            break

        # Validar movimiento
        if not pila_origen:  # Torre de origen vacía
            secuencia_invalida = True
            break

        disco = pila_origen[-1]  # Disco superior de la torre origen
        if pila_destino and pila_destino[-1] < disco:  # Regla: no colocar disco grande sobre pequeño
            secuencia_invalida = True
            break

        # Realizar el movimiento
        pila_origen.pop()
        pila_destino.append(disco)

    # Determinar el resultado del caso
    if secuencia_invalida:
        print("secuencia invalida")
    elif not torre_A and not torre_B and torre_C == list(range(n, 0, -1)):
        print("soluciona la torre")
    else:
        print("no soluciona la torre")
