from src.Lab4.RapidPotentiation import FastDiscretePotentiating, GeneratePrimeNumber, LargestCommonDivisor


def main():
    message = int(input('Input the message: '))
    publicExponent = int(input('Input the public key1(exponent): '))
    publicModulus = int(input('Input public key2(modulus): '))
    print(f"----------------- result -----------------")
    print(f'\"Encrypted message\": {FastDiscretePotentiating(message, publicExponent, publicModulus)}')
    print(f"------------------------------------------")

    print('\n')
    p_max = int(input('Input P-max number: '))
    while True:
        simpleSmallNumber = int(input('Input small simple number: '))
        if LargestCommonDivisor(simpleSmallNumber) == simpleSmallNumber:
            print(f'\nPrime number was generated P= {GeneratePrimeNumber(p_max, simpleSmallNumber)}')
            break
        else:
            print(f"\nThe small number entered is not prime. Try again!")


if __name__ == '__main__':
    main()
