dic = {}
while True:
    palabra = input().strip()
    if palabra == "#":
        break
    dic[palabra] = True
compuestas = []

for palabra in dic:
    for i in range(1, len(palabra)):
        parte1 = palabra[:i]
        parte2 = palabra[i:]
        if parte1 in dic and parte2 in dic:
            compuestas.append((palabra, parte1, parte2))

compuestas.sort()
for compuesta, parte1, parte2 in compuestas:
    print(f"{compuesta} = {parte1} + {parte2}")