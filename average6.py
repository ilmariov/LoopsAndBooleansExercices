def main():
    filename = input('What file are the numbers in? ')
    infile = open(filename, 'r')
    total = 0.0
    count = 0
    line = infile.readline()
    while line != '':
        total = total + float(line)
        count = count + 1
        line = infile.readline()
    print('The average of the numbers is', total/count)

main()