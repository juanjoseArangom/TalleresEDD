c = int(input())
for _ in range(c):
    n, p = map(int, input().split())
    conjunto = list(map(int, input().split()))
    divisores_p = set()  
    for i in range(1, int(p**0.5) + 1):
        if p % i == 0:  
            divisores_p.add(i)  
            if i != p // i: 
                divisores_p.add(p // i)
    if divisores_p.issubset(set(conjunto)):
        print("Es PrimiConjunto")
    else:
        print("No es PrimiConjunto")