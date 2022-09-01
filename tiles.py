import math

def movingTiles(l, s1, s2, queries):
    ds = abs(s2 - s1)
    time_array = []
    for i in range(len(queries)):
        dx = l - math.sqrt(queries[i])
        delta_displacement = dx / math.cos(math.pi / 4)
        time = delta_displacement / ds
        time_array.append(time)
    return time_array

def main():
    result = movingTiles(10, 1, 2, [50, 100])
    print (result)

main()