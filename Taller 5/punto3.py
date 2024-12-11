from collections import deque

pila = deque()  
while True:
    entrada = input().split()
    if entrada[0] == "termina":
        break
    elif entrada[0] == "agrega":
        pila.append(int(entrada[1]))
    elif entrada[0] == "engulle":
        if len(pila) > 1:
            if pila[0] > pila[-1]:
                pila.pop()
            else:
                pila.popleft()
        elif len(pila) == 1:
            pila.pop()
        else:
            continue
if pila:
    print("cabeza", pila[0], "cola", pila[-1])

