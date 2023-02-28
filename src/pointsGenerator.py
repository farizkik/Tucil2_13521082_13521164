import random

def generateRandomPoints():
    # validasi input
    while True:
        n = input("How many points to be randomly generated: ") # number of points to generate
        if (n.isdigit() and int(n) > 1):
            n = int(n)
            break
        elif(n.isdigit() == False):
            print("Input must be an integer\n")
        else:
            print("There's should be atleast 2 points to do so!\n")
    while True:
        N = input("Input the dimension: ") # number of dimension (in space R^N)
        if (N.isdigit() and int(N) > 0):
            N = int(N)
            break
        elif(N.isdigit() == False):
            print("Input must be an integer\n")
        else:
            print("The dimension should be atleast 1\n")

    points = []

    for i in range(n):
        point = []
        for j in range(N):
            # random float between 1000000 and 1000000
            # array representing the point, rounded to 3 floating numbers
            if(N<=5):
                point.append(round(random.uniform(-10000, 10000), 3))
            else:
                point.append(round(random.uniform(-1000, 1000), 3))
        points.append(point)
    return points, N