import rsa


def GenerateKeysAndWriteToFile() -> None:
    """
    Generates public and private keys for the RSA encryption algorithm
    and write this keys to the file publicKey.pem and privateKey.pem
    """
    (publicKey, privateKey) = rsa.newkeys(1024)
    with open('publicKey.pem', 'wb') as publicKeyFile:
        publicKeyFile.write(publicKey.save_pkcs1('PEM'))

    with open('privateKey.pem', 'wb') as privateKeyFile:
        privateKeyFile.write(privateKey.save_pkcs1('PEM'))


def LoadKeys() -> (str, str):
    """
    Read public and private keys for RSA encryption algorithm from files
    publicKey.pem and privateKey.pem
    """
    with open('publicKey.pem', 'rb') as publicKeyFile:
        publicKey = rsa.PublicKey.load_pkcs1(publicKeyFile.read())

    with open('privateKey.pem', 'rb') as privateKeyFile:
        privateKey = rsa.PrivateKey.load_pkcs1(privateKeyFile.read())

    return publicKey, privateKey


def EncryptRSA(message, key):
    return rsa.encrypt(message.encode('ascii'), key)


def DecryptRSA(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except():
        return UnicodeDecodeError


def SignSha1(message, key):
    return rsa.sign(message.encode('ascii'), key, 'SHA-1')


def VerifySha1(message, signature, key):
    try:
        return rsa.verify(message.encode('ascii'), signature, key) == 'SHA-1'
    except():
        return KeyError()