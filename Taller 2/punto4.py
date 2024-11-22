n = int(input())
arreglo = tuple(input().split(", "))
inicio = 0
fin = n - 1

resultado = ()
while inicio <= fin:
    resultado += (arreglo[inicio],)
    inicio += 1
    if inicio <= fin:
        resultado += (arreglo[fin],)
        fin -= 1
print("".join(resultado))