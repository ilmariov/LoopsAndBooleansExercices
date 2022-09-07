# A program that computes the fuel efficiency of a multi-leg journey.

def main():
    try:
        start_odo = float(input('Set the starting odometer reading (in miles): '))
        odo1 = odo2 = start_odo
        route = total_gas = 0
        print('Enter the following data separated by a space\n')

        while odo2 != '':
            leg = input('Current odometer reading (miles) - amount of gas used (gallons)): ')
            if leg != '':
                leg = leg.split()
                odo2, gas = float(leg[0]), float(leg[1])
                miles_per_leg = odo2 - odo1
                mpg_per_leg = miles_per_leg / gas
                print('MPG achieved in this leg: {0}'.format(mpg_per_leg))
                odo1 = odo2
                route = route + miles_per_leg
                total_gas = total_gas + gas
            else:
                odo2 = leg
        
        print('The total MPG for the trip is: {0}'.format(route/total_gas))

    except:
        print('Enter data according instructions')
        
main()