from DNC import *
from bruteForce import *
from pointsGenerator import *
from utilities import *

points, dimension = generateRandomPoints()

# print(bruteForceClosestPairnD(points))
# print(closestPairnD(points))

result = closestPairnD(points)
minDist = result[0]
closest_pair = result[1]

if (dimension == 3):
    visualize3D(points, closest_pair)
elif (dimension == 2):
    visualize2D(points, closest_pair)
elif (dimension == 1):
    visualize1D(points, closest_pair)