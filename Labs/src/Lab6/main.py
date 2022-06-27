from src.Lab6.BLL.Operations import *
from Crypto.Cipher import DES3


def main():
    print('Це програма шифрування і дешифрування тексту.')

    counter = True
    key = KeyGeneration()

    while counter:
        mode = input('Введіть 1 якщо бажаєте зашифрувати текст: ')
        if mode == '1':
            text = input('Введіть текст, який бажаєте зашифрувати: ')
            baseText = examination(text)

            des = DES3.new(key, DES3.MODE_ECB)

            encryptedText = DesEncrypt(baseText, des)
            output_encrypted_text = input('Вивести зашифрований текст?(y/n)')
            if output_encrypted_text == 'y':
                print('Зашифрований текст: ', encryptedText)

            decryptedText = DesDecrypt(encryptedText, des)
            outputDecryptedText = input('Вивести результати дешифрування?(y/n)')
            if outputDecryptedText == 'y':
                print('Розшифрований текст: ', decryptedText)

            text = input('1 - Зберегти поточний ключ;'
                         '2 - згенерувати новий ключ;')
            if text == '2':
                key = KeyGeneration()

        else:
            counter = False


if __name__ == '__main__':
    main()
