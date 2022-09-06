def main():
    m = int(input('Enter first positive integer: '))
    n = int(input('Enter second positive integer: '))
    if m < n:
        a = n
        b = m
    else:
        a = m
        b = n
    rem = a % b
    while rem != 0:
        a = b
        b = rem
        rem = a % b
    print('The greatest common divisor of {0} and {1} is: {2}'.format(m, n, b))

main()
    