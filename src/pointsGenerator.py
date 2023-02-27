import random

def generateRandomPoints():
    n = int(input("How many points to be randomly generated: ")) # number of points to generate
    N = int(input("Input the dimension: ")) # number of dimension (in space R^N)
    points = []

    for i in range(n):
        point = []
        for j in range(N):
            # random float between 1000000 and 1000000
            # array representing the point, rounded to 3 floating numbers
            point.append(round(random.uniform(-10**6, 10**6), 3))
        points.append(point)
    return points

#print(generateRandomPoints())