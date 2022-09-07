def main():
    try:
        heating_deg = cooling_deg = 0

        while True:
            avg_temp = input('Enter average daily temperature (<Enter> to quit): ')
            if avg_temp != '':
                avg_temp = float(avg_temp)
                if avg_temp < 60:
                    heating_deg = heating_deg + (60 - avg_temp)
                elif avg_temp > 80:
                    cooling_deg = cooling_deg + (avg_temp - 80)
            else:
                break

        print('Heating degrees: {0} \nCooling degrees: {1}'.format(heating_deg, cooling_deg))

    except:
        print('Enter a valid number')

main()