def main():
    x = int(input('Enter a natural number: '))
    syrSeq = [x]
    print('The Syracuse sequence starting with {0} is:'.format(x))

    while x !=1 :
        if x % 2 == 0:
            x = int(x / 2)
            syrSeq.append(x)
        else:
            x = 3 * x + 1
            syrSeq.append(x)
    
    print(syrSeq)

main()