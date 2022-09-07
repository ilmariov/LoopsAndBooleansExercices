def main():
    try:
        infilename = input('Enter filename with info of journey: ')
        infile = open(infilename, 'r')

        for i in range(1):
            first_line = infile.readline()
        start_odo = float(first_line)        
        odo1 = odo2 = start_odo
        route = total_gas = 0

        for line in infile:
            if line != '' and line != first_line:
                leg = line.split()
                odo2, gas = float(leg[0]), float(leg[1])
                miles_per_leg = odo2 - odo1
                mpg_per_leg = miles_per_leg / gas
                print('MPG achieved in this leg: {0:0.2f}'.format(mpg_per_leg))
                odo1 = odo2
                route = route + miles_per_leg
                total_gas = total_gas + gas
            
        print('The total MPG for the trip is: {0:0.2f}'.format(route/total_gas))

    except:
        print('Something wrong happened')

main()