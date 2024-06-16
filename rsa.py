from rsa_keygen import RSAKeyGenerator, prime_gen

class RSAOperations:
    @staticmethod
    def ModPotenzieren(x, y, n):
        return pow(x, y, n)

    @staticmethod
    def verschluesseln(key, klartext):
        e, n = key
        geheimtext = RSAOperations.ModPotenzieren(klartext, e, n)
        return geheimtext

    @staticmethod
    def entschluesseln(key, geheimtext):
        d, n = key
        klartext = RSAOperations.ModPotenzieren(geheimtext, d, n)
        return klartext

def main():
    prime_generator = prime_gen()
    rsa_keygen = RSAKeyGenerator(prime_generator)
    rsa_keygen.generate_keys()

    public_key = rsa_keygen.get_public_key()
    private_key = rsa_keygen.get_private_key()

def is_module():
    pass # TODO: Implement this function

if __name__ == '__main__':
    main()
else:
    is_module()