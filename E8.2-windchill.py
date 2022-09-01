def printTable(a, b, c, d, e, f, g, h, i, j):
    print("{0:^9} {1:^9} {2:^9} {3:^9} {4:^9} {5:^9} {6:^9} {7:^9} {8:^9} {9:^9}"
        .format(a, b, c, d, e, f, g, h, i, j))

def main():
    printTable("V \ T", -20, -10, 0, 10, 20, 30, 40, 50, 60)

    for i in range(0, 55, 5):
        wI = [i]
        if i <= 3:
            printTable(wI[0], "-", "-", "-", "-", "-", "-", "-", "-", "-")
        else:
            for j in range(-20, 70, 10):
                windchillIndex = 35.74 + (0.6215 * j) - (35.75 * (i ** 0.16)) + (0.4275 * j * (i ** 0.16))
                wI.append("{0:0.3}".format(windchillIndex))
            printTable(wI[0], wI[1], wI[2], wI[3], wI[4], wI[5], wI[6], wI[7], wI[8], wI[9])

main()