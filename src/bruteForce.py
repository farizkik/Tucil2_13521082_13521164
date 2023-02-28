from utilities import *

# Brute Force Algorithm for Finding Closest Pair of Points
def bruteForceClosestPair3D(points):
    n_euclidean_computing = 0
    n = len(points)
    min_distance = inf
    closest_pair = []
    for i in range(n):
        for j in range(i+1, n):
            distance = sqrt((points[i][0]-points[j][0])**2 + 
                                 (points[i][1]-points[j][1])**2 +
                                 (points[i][2]-points[j][2])**2)
            n_euclidean_computing += 1
            if (distance < min_distance):
                min_distance = distance
                closest_pair = []
                closest_pair.append([points[i], points[j]])
            elif (distance == min_distance):
                closest_pair.append([points[i], points[j]])
    return [min_distance, closest_pair, n_euclidean_computing]

def bruteForceClosestPairnD(points):
    n_euclidean_computing = 0
    n = len(points)
    min_distance = inf
    closest_pair = None
    for i in range(n):
        for j in range(i+1, n):
            distance = sqrt(sum([(points[i][k]-points[j][k])**2 for k in range(len(points[i]))]))
            n_euclidean_computing += 1
            if (distance < min_distance):
                min_distance = distance
                closest_pair = []
                closest_pair.append([points[i], points[j]])
            elif (distance == min_distance):
                closest_pair.append([points[i], points[j]])
    return [min_distance, closest_pair, n_euclidean_computing]