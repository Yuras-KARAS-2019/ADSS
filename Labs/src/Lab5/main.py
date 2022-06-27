from src.Lab5.BLL.RSAOperations import *


def main():
    GenerateKeysAndWriteToFile()
    publicKey, privateKey = LoadKeys()
    message = input('Enter a message:')

    ciphertext = EncryptRSA(message, publicKey)
    signature = SignSha1(message, privateKey)
    plaintext = DecryptRSA(ciphertext, privateKey)

    print(f'Cipher text: {ciphertext}')
    print(f'Signature: {signature}')

    if plaintext:
        print(f'Decrypted message: {int(plaintext)}')
    else:
        print('Could not decrypt the message.')

    if VerifySha1(plaintext, signature, publicKey):
        print('Signature verified!')
    else:
        print('message signature not verified')


if __name__ == "__main__":
    main()