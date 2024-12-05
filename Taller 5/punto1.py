entrada = input().split()
n, t = int(entrada[0]), int(entrada[1])
vendedores = []
for _ in range(n):
    cc, boletas = map(int, input().split())
    vendedores.append((cc, boletas))
    t -= boletas
while len(vendedores) > 1 or t > 0:
    vendedores.pop((len(vendedores) -1) % 5)
print(vendedores)

    
    