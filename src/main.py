from DNC import *
from bruteForce import *
from pointsGenerator import *
from utilities import *
from timeit import default_timer as timer

points, dimension = generateRandomPoints()

start=timer()
print(bruteForceClosestPairnD(points))
end=timer()
print("Bruteforce time: " + str(end-start)+ " s") 

start=timer()
print(closestPairnD(points))
end=timer()
print("Divide and Conquer time: " + str(end-start)+ " s") 
'''
result = closestPairnD(points)
minDist = result[0]
closest_pair = result[1]


if (dimension == 3):
    visualize3D(points, closest_pair)
elif (dimension == 2):
    visualize2D(points, closest_pair)
elif (dimension == 1):
    visualize1D(points, closest_pair)
    '''