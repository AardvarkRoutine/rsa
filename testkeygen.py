from rsa_keygen import RSAKeyGenerator, prime_gen  # Assuming rsa_keygen.py is the module name

prime_generator = prime_gen()
rsa_keygen = RSAKeyGenerator(prime_generator)
rsa_keygen.generate_keys()

public_key = rsa_keygen.get_public_key()
private_key = rsa_keygen.get_private_key()

print("Public key:", public_key)
print("Private key:", private_key)