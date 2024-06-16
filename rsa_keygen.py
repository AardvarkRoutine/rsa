# Programm von Oskar und Paul
import random
import math

class prime_gen:
    def __init__(self, limit=10000):
        self.primes = list(self.sieve(limit))
        random.shuffle(self.primes)

    def sieve(self, limit):
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

    def get_prime(self):
        if not self.primes:
            raise ValueError("No more unique primes available.")
        return self.primes.pop()

class RSAKeyGenerator:
    def __init__(self, prime_generator):
        self.prime_generator = prime_generator
        self.public_key = None
        self.private_key = None

    def generate_keys(self):
        p = self.prime_generator.get_prime()
        q = self.prime_generator.get_prime()

        while p == q:
            q = self.prime_generator.get_prime()

        n = p * q

        phi_n = (p - 1) * (q - 1)

        e = 65537
        if math.gcd(e, phi_n) != 1:
            e = self.find_coprime(phi_n)

        d = self.mod_inverse(e, phi_n)

        self.public_key = (e, n)
        self.private_key = (d, n)

    def get_public_key(self):
        if self.public_key is None:
            raise ValueError("Keys have not been generated yet.")
        return self.public_key

    def get_private_key(self):
        if self.private_key is None:
            raise ValueError("Keys have not been generated yet.")
        return self.private_key

    def find_coprime(self, phi_n):
        e = 2
        while e < phi_n:
            if math.gcd(e, phi_n) == 1:
                return e
            e += 1
        raise ValueError("No coprime e found.")

    def extended_gcd(self, a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = self.extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    def mod_inverse(self, e, phi_n):
        gcd, x, y = self.extended_gcd(e, phi_n)
        if gcd != 1:
            raise ValueError("Modular inverse does not exist")
        else:
            return x % phi_n
        