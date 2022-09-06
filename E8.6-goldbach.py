import math

def is_prime(n):
    d2 = math.sqrt(n) // 1       # upper limit of divisor
    x = 1                        # prime checker: 1 --> yes, 0 --> no
    while d2 >= 2:
        isPrime = n / d2
        if isPrime.is_integer():
            x = 0
            break
        d2 = d2 - 1
    return x

def main():
    while True:
        n = int(input('Enter an even natural number: '))
        if n % 2 == 0:
            break
    print('Possible combinations of prime numbers that equal {0} when added:\n'.format(n))
    
    for i in range(int(n/2), 0, -1):
        if is_prime(i) == 1:            # is prime
            for j in range(int(n/2), n):
                if is_prime(j) == 1 and i + j == n:    # is prime
                    print ('{0} + {1} = {2}'.format(i, j, n))

main()