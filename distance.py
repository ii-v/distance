#!/usr/bin/python3
# ----------------------------------------------------------------- #
# Calculates the distance between two points in a coordinate system #
# ----------------------------------------------------------------- #

from math import hypot
from sys import argv


def calculateDistance(x1, y1, x2, y2):
    distance = hypot(x1 - y1, x2 - y2)
    return distance


def main():
    errorMessage = "Usage:\n\t{} [x1 y1 x2 y2]".format(argv[0])
    try:
        distance = calculateDistance(float(argv[1]), float(argv[2]),
                                     float(argv[3]), float(argv[4]))
        print(distance)
    except:
        print(errorMessage)

if __name__ == "__main__":
    main()
