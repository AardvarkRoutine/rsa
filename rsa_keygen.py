import random
import math

def sieve(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (is_prime[p] == True):
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    for p in range(256, limit + 1):
        if is_prime[p] and len(str(p)) == 4:
            yield p

class prime_gen:
    def __init__(self, limit=10000):
        self.primes = list(sieve(limit))
        random.shuffle(self.primes)

    def get_prime(self):
        if not self.primes:
            raise ValueError("No more unique primes available.")
        return self.primes.pop()
    
prime_generator = prime_gen()



