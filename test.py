def main():
    num = abs(int(input("Enter a whole number: ")))
    count = 0
    while num != 1:
        num = num // 2
        count = count + 1

    print (count)

main()