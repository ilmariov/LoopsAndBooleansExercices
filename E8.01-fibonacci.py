def fibonacci(n):
    b1 = -1
    b2 = 0
    for i in range(n):
        fibo = abs(b1+b2)
        b1 = b2
        b2 = fibo
    return fibo

def main():
    n = int(input("Enter the n-th Fibonacci number you want to know: "))
    fibo = fibonacci(n)
    print('The {0}-th fibonacci number is: {1}'.format(n, fibo))

main()