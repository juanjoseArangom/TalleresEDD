n = int(input())
jso = tuple(map(int, input().split(", ")))
jlar = tuple(map(int, input().split(", ")))
jis = tuple(map(int, input().split(", ")))
pso = 0
plar = 0
pis = 0
for i in range(n):
    if jso[i] % 2 == 0 and (jso[i] + jlar[i] + jis[i]) % 2 == 0:
        pso += 1
    elif jso[i] % 2 != 0 and (jso[i] + jlar[i] + jis[i]) % 2 != 0:
        pso += 1
    if jlar[i] % 2 == 0 and (jso[i] + jlar[i] + jis[i]) % 2 == 0:
        plar += 1
    elif jlar[i] % 2 != 0 and (jso[i] + jlar[i] + jis[i]) % 2 != 0:
        plar += 1
    if jis[i] % 2 == 0 and (jso[i] + jlar[i] + jis[i]) % 2 == 0:
        pis += 1
    elif jis[i] % 2 != 0 and (jso[i] + jlar[i] + jis[i]) % 2 != 0:
        pis += 1
print("SO:"+ str(pso) + ", LAR:" + str(plar) + ", IS:" + str(pis))       

# n = int(input())
# data = [tuple(map(int, input().split())) for _ in range(3)]  # Agrupa jso, jlar, jis
# counters = [0, 0, 0]  # Contadores para SO, LAR, IS

# for i in range(n):
#     total_mod = sum(row[i] for row in data) % 2  # Suma total mod 2
#     for j, row in enumerate(data):
#         if row[i] % 2 == total_mod:  # Verifica condición
#             counters[j] += 1

# print(f"SO:{counters[0]}, LAR:{counters[1]}, IS:{counters[2]}")