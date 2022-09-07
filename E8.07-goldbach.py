import math

def is_prime(n):
    d2 = math.sqrt(n) // 1       # upper limit of divisor
    while d2 >= 2:
        isPrime = n / d2
        if isPrime.is_integer():
            return False
        d2 = d2 - 1
    return True

def main():
    while True:
        n = int(input('Enter an even natural number: '))
        if n % 2 == 0:
            break
    print('Possible combinations of prime numbers that equal {0} when added:\n'.format(n))
    
    for i in range(int(n/2), 0, -1):
        if is_prime(i):
            for j in range(int(n/2), n):
                if is_prime(j) and i + j == n:
                    print ('{0} + {1} = {2}'.format(i, j, n))

main()