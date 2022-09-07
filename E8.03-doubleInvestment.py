# This program calculates how long it takes for an invesment 
# to double at a given interest rate

def main():
    initial = 1
    principal = initial
    years = 0
    apr = eval(input("Enter the annual interest rate: "))

    while True:
        principal = principal * (1 + apr / 100)
        if principal > (initial * 2):
            break
        years = years + 1

    print('It takes {0} years for an investment to double at an annualized interest rate of {1}%'.format(years, apr))

main()