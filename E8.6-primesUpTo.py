import math

def main():
    n = int(input('Enter a positive whole number: '))
    primes = []
    for i in range(1, n+1):
        x = 1                        # prime checker: 1 --> yes, 0 --> no
        d2 = math.sqrt(i) // 1       # greatest possible divisor
        while d2 >= 2:
            isPrime = i / d2
            if isPrime.is_integer():
                x = 0
                break
            d2 = d2 - 1
        if x == 1:
            primes.append(i)
    print('Primes up to {0}:\n {1}'.format(n, primes))

main()