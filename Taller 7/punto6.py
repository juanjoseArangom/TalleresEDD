N = 6
valores = [13, 27, 9, 45, 36, 18]
eliminados = []

while len(valores) > 0:
    max_residuo = -1
    indice_a_eliminar = -1
    for i in range(len(valores)):
        residuo = valores[i] % len(valores)
        if residuo > max_residuo:
            max_residuo = residuo
            indice_a_eliminar = i
    eliminados.append(valores.pop(indice_a_eliminar))

for elemento in eliminados:
    print(elemento)
