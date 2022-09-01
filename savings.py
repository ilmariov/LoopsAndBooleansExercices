def main():
    monthlySaving = int(input('Enter amount to save monthly: '))
    interestRate = float(input('Enter anual interest rate: '))
    numOfMonths = int(input('Enter number of months to save: '))
    accumulated = 0

    for i in range(numOfMonths):
        accumulated = accumulated + monthlySaving
        accumulated = accumulated * (1 + (interestRate / 12)/100)
    
    print(accumulated)

main()