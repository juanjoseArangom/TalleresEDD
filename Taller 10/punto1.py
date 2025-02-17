n = int(input())
dic = {}
for _ in range(n):
    entrada = input().split()
    dic[entrada[0]] = entrada[1]
while True:  
    entrada = input()
    if entrada == "#":
        break  
    elif entrada in dic:
        print(dic[entrada])
    else:
        print("Entrada no encontrada")