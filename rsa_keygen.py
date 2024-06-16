import random

def sieve(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (is_prime[p] == True):
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = []
    for p in range(256, limit + 1):
        if is_prime[p]:
            prime_numbers.append(p)
    return prime_numbers

class PrimeGenerator:
    def __init__(self, limit=10000):
        self.primes = sieve(limit)
        random.shuffle(self.primes)

    def get_prime(self):
        if not self.primes:
            raise ValueError("No more unique primes available.")
        return self.primes.pop()

prime_gen = PrimeGenerator()

print(prime_gen.get_prime())
print(prime_gen.get_prime())
print(prime_gen.get_prime())
print(prime_gen.get_prime())
print(prime_gen.get_prime())
