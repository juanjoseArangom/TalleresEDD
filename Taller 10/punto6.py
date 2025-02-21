def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    # Leer la cantidad de casos de prueba
    C = int(data[0])
    cases = [int(data[i]) for i in range(1, C + 1)]
    
    # Encontrar el máximo N para generar primos hasta ese valor
    max_N = max(cases)
    
    # Generar todos los números primos hasta max_N usando la criba de Eratóstenes
    sieve = [True] * (max_N + 1)
    sieve[0] = sieve[1] = False  # 0 y 1 no son primos
    for p in range(2, int(max_N**0.5) + 1):
        if sieve[p]:
            for multiple in range(p * p, max_N + 1, p):
                sieve[multiple] = False
    primes = [p for p, is_prime in enumerate(sieve) if is_prime]
    
    # Para cada caso, contar las parejas de primos que suman N
    for N in cases:
        count = 0
        for p in primes:
            if p > N // 2:
                break  # Evitar duplicados (p, q) y (q, p)
            q = N - p
            if sieve[q]:
                count += 1
        print(count)
 
if __name__ == "__main__":
    main()