n = int(input())
for _ in range(n):
    expresion = input().replace(" ", "").rstrip(';')  
    pila = []
    correcta = True
    for simbolo in expresion:
        if simbolo in "({[":
            pila.append(simbolo)  
        elif simbolo in ")}]":
            if not pila:
                correcta = False
                break
            ultimo = pila.pop()  
            if (simbolo == ')' and ultimo != '(') or \
               (simbolo == '}' and ultimo != '{') or \
               (simbolo == ']' and ultimo != '['):
                correcta = False
                break
    if correcta and not pila:
        print("correcta")
    else:
        print("incorrecta")