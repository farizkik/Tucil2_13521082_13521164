from DNC import *
from bruteForce import *
from pointsGenerator import *
from utilities import *
import time

points, dimension = generateRandomPoints()

# Finding Closest Pair with Brute Force Approach
start = time.time()
result = bruteForceClosestPairnD(points)
end = time.time()

print("\nWith Brute Force Approach:")
print("the closest pair are between:", end=" ")
print(result[1])
print("with the minimum distance:", round(result[0], 3))
print("the euclidean operation executed by:", result[2], "times")
print("and execution time within:", end=" ")
print("{0:.10f}".format(end-start), "seconds")


# Finding Closest Pair with Divide n Conquer Approach
start = time.time()
result = closestPairnD(points)
end = time.time()

print("\nWith Divide and Conquer Approach:")
print("the closest pair are between:", end=" ")
print(result[1])
print("with the minimum distance:", round(result[0], 3))
print("the euclidean operation executed by:", result[2], "times")
print("and execution time within:", end=" ")
print("{0:.10f}".format(end-start), "seconds\n")

# Asking for visualization
if (dimension == 3):
    while True:
        visualize = input("Do you want to visualize the points? (y/n): ")
        if (visualize == 'y'):
            visualize3D(points, result[1])
            break
        elif (visualize == 'n'):
            break
        else:
            print("Invalid input!")

elif (dimension == 2):
    while True:
        visualize = input("Do you want to visualize the points? (y/n): ")
        if (visualize == 'y'):
            visualize2D(points, result[1])
            break
        elif (visualize == 'n'):
            break
        else:
            print("Invalid input!")

elif (dimension == 1):
    while True:
        visualize = input("Do you want to visualize the points? (y/n): ")
        if (visualize == 'y'):
            visualize1D(points, result[1])
            break
        elif (visualize == 'n'):
            break
        else:
            print("Invalid input!")