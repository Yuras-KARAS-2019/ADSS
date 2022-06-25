import math


# -------------------------- Lab 4.1 --------------------------
def FastDiscretePotentiating(base, publicExponent, publicModulus):
    """
    this function performs fast discrete potentiating"""

    binaryPublicExponent = bin(publicExponent).replace('0b', '')
    resultCipher = 1
    for i in range(len(binaryPublicExponent)):
        resultCipher = ((resultCipher ** 2) * (base ** int(binaryPublicExponent[i]))) % publicModulus
    return resultCipher


# -------------------------- Lab 4.2 --------------------------
def GeneratePrimeNumber(p_max, simpleSmallNumber):
    """
    this function generates prime numbers"""

    k = math.ceil(math.log(p_max / 2, simpleSmallNumber))
    p1 = 2 * (simpleSmallNumber ** k) + 1
    p2 = 2 * (simpleSmallNumber ** k) - 1
    if FastDiscretePotentiating(2, p1 - 1, p1) == 1:
        p = p1
    elif FastDiscretePotentiating(2, p2 - 1, p2) == 1:
        p = p2
    else:
        while FastDiscretePotentiating(2, p1 - 1, p1) != 1:
            p1 += 2
        p = p1
    return p


def LargestCommonDivisor(number):
    """
    this function returns the largest common divisor"""

    d = 2
    while number % d != 0:
        d += 1
    return d
