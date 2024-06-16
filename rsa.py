# Programm von Oskar und Paul
from rsa_keygen import RSAKeyGenerator, prime_gen

def ModPotenzieren(x, y, n):
    return pow(x, y, n)

def verschluesseln(key, klartext):
    e, n = key
    geheimtext = ModPotenzieren(klartext, e, n)
    return geheimtext

def entschluesseln(key, geheimtext):
    d, n = key
    klartext = ModPotenzieren(geheimtext, d, n)
    return klartext

''' 
Die Funktionen primfaktoren, extended_gcd und multInv sind hier erneut
definiert, da test_2_RSA.py nicht über rsa.py auf rsa_keygen.py zugreifen
kann (wo diese eigentlich gebraucht werden).
'''

def primfaktoren(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def multInv(e, phi):
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

def main():
    prime_generator = prime_gen()
    rsa_keygen = RSAKeyGenerator(prime_generator)
    rsa_keygen.generate_keys()
    private_key = rsa_keygen.get_private_key()
    public_key = rsa_keygen.get_public_key()
    print("Do you want to encrypt or decrypt? (e/d)")
    choice = input()
    if choice == "e":
        print("Enter the plaintext:")
        plaintext = input()
        ciphertext = [verschluesseln(public_key, ord(char)) for char in plaintext]
        print(f"Ciphertext: {ciphertext}, public key: {public_key}, private key: {private_key}")
    elif choice == "d":
        print("Enter the ciphertext as a list of numbers:")
        ciphertext = list(map(int, input().strip('[]').split(',')))
        print("Enter the private key in the format 'd,n':")
        private_key_input = input()
        d, n = map(int, private_key_input.split(','))
        private_key = (d, n)
        
        plaintext = ''.join(chr(entschluesseln(private_key, char)) for char in ciphertext)
        print("Plaintext:", plaintext)
    else:
        print("Invalid choice. Exiting...")

if __name__ == '__main__':
    main()
