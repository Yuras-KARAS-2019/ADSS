import random


def examination(text):
    while len(text) % 8 != 0:
        text += ' '
    return text


def DesEncrypt(text, des):
    return des.encrypt(text.encode('utf-8'))


def DesDecrypt(text, des):
    return des.decrypt(text).decode().rstrip('')


def KeyGeneration():
    symbols = list('qwertyuiopasdfghjklzxcvbnm1234567890+-/*.,<>/?\|_!@#$%^&()~')
    key_list = ''
    for i in range(24):
        key_list += random.choice(symbols)

    return bytes(str(key_list), encoding='utf-8')
