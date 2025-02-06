import heapq
adentro = []
while True:
    entrada = input().split()
    if entrada[0] == "fin":
        break
    if entrada[0] == "ingresa":
        valor = int(entrada[1])
        if adentro:
            grande = heapq.heappop(adentro)
            if -valor <= grande / 2:
                heapq.heappush(adentro, -valor) 
                print("adelante")
            else:
                print("denegado")
            heapq.heappush(adentro, grande)
        else:
            heapq.heappush(adentro, -valor)
            print("adelante")
    elif entrada[0] == "salida":
        if adentro:
            heapq.heappop(adentro)
            print("hasta pronto")
    