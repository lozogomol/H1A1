import math

def sieve(n):
    """Devuelve todos los primos hasta n usando la criba de Eratóstenes."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    primes = [i for i, val in enumerate(is_prime) if val]
    return primes

def count_primes_in_range(L, R, primes):
    """Cuenta los primos entre L y R usando la criba segmentada."""
    n = R - L + 1
    is_prime_range = [True] * n
    for p in primes:
        start = max(p * p, ((L + p - 1) // p) * p)
        for j in range(start, R + 1, p):
            is_prime_range[j - L] = False
    if L == 1:
        is_prime_range[0] = False
    return sum(is_prime_range)

# Leer todos los casos de prueba
primes = sieve(int(1e4))  # √(10^8) ≈ 10000
while True:
    line = input()
    L, R = map(int, line.split())
    if L == 0 and R == 0:
        break
    print(count_primes_in_range(L, R, primes))
