from collections import deque
c = int(input())
for _ in range(c):
    pila = deque(map(int, input().split()))
    while len(pila) > 1:
        suma = pila[-1] + pila[-2]
        if suma % 2 == 0:
            pila.pop()
            pila.pop()
            pila.append(suma/2)
        else:
            break
    print(len(pila), int(pila[-1]))