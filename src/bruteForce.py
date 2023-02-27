from utilities import *


# Brute Force Algorithm for Finding Closest Pair of Points
def bruteForceClosestPair3D(points):
    n_euclidean_computing = 0
    n = len(points)
    min_distance = inf
    closest_pair = None
    for i in range(n):
        for j in range(i+1, n):
            distance = sqrt((points[i][0]-points[j][0])**2 + 
                                 (points[i][1]-points[j][1])**2 +
                                 (points[i][2]-points[j][2])**2)
            n_euclidean_computing += 1
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])
    return closest_pair, n_euclidean_computing

def bruteForceClosestPairnD(points):
    n_euclidean_computing = 0
    n = len(points)
    min_distance = inf
    closest_pair = None
    for i in range(n):
        for j in range(i+1, n):
            distance = sqrt(sum([(points[i][k]-points[j][k])**2 for k in range(len(points[i]))]))
            n_euclidean_computing += 1
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])
    return [min_distance,closest_pair, n_euclidean_computing]

'''
# Testing
points3D = [[2, 3.4, -5.02], [-9, -2.54, 0], [6, 6, 6], [9, 4.7, 0.2631], [9.23, 0.3, 7.3], [2, 4, 1], [7, 2, 3]]
closest_pair, n_Computing = bruteForceClosestPair3D(points3D)
# bruteForceClosestPair3D, nComputing = bruteForceClosestPair3D(points3D)
print("Titik terdekat adalah", closest_pair)
print("Dengan jarak", round(euclideanDistance(closest_pair[0], closest_pair[1]), 3))
print("banyaknya operasi euclidean", n_Computing)
'''