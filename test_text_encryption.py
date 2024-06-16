from rsa import *
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
        ciphertext = verschluesseln(public_key, plaintext)
        print(f"Ciphertext: {ciphertext}, public key: {public_key}, private key: {private_key}")
    elif choice == "d":
        print("Enter the ciphertext as a list of numbers:")
        ciphertext = list(map(int, input().strip('[]').split(',')))
        print("Enter the private key in the format 'd,n':")
        private_key_input = input()
        d, n = map(int, private_key_input.split(','))
        private_key = (d, n)
        
        plaintext = entschluesseln(private_key, ciphertext)
        print("Plaintext:", plaintext)
    else:
        print("Invalid choice. Exiting...")

if __name__ == '__main__':
    main()