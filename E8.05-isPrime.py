import math

def main():
    try:
        n = int(input('Enter a positive whole number greater than 2: '))
        d2 = math.sqrt(n) // 1       # upper limit of divisor
        x = 1                        # prime checker: 1 --> yes, 0 --> no

        while d2 >= 2:
            isPrime = n / d2
            if isPrime.is_integer():
                x = 0
                break
            d2 = d2 - 1

        if x == 0:
            print('Is Not Prime')
        else:
            print('Is Prime')

    except:
        print('Try again entering a positive whole number greater than 2.')

main()