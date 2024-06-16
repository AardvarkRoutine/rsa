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

def main():
    prime_generator = prime_gen()
    rsa_keygen = RSAKeyGenerator(prime_generator)
    rsa_keygen.generate_keys()

    public_key = rsa_keygen.get_public_key()
    private_key = rsa_keygen.get_private_key()

    print("Do you want to encrypt or decrypt? (e/d)")
    choice = input()
    if choice == "e":
        print("Enter the plaintext:")
        plaintext = int(input())
        ciphertext = verschluesseln(public_key, plaintext)
        print(f"Ciphertext: {ciphertext}, public key: {public_key}, private key: {private_key}")
    elif choice == "d":
        print("Enter the ciphertext:")
        ciphertext = int(input())
        print("Enter the private key in the format 'd,n':")
        private_key_input = input()
        d, n = map(int, private_key_input.split(','))
        private_key = (d, n)
        
        plaintext = entschluesseln(private_key, ciphertext)
        print("Plaintext:", plaintext)
    else:
        print("Invalid choice. Exiting...")

def is_module():
    pass # TODO: Implement this function

if __name__ == '__main__':
    main()
