from math import *
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

# Merge Sort Algorithm Using Divide and Conquer Approach for Array
# in default, sorting would be ascending
def mergeSort(arr, asc = 1):
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    left_arr = mergeSort(left_arr, asc)
    right_arr = mergeSort(right_arr, asc)

    # conquer
    return merge(left_arr, right_arr, asc)


# conquer implementation
def merge(left_arr, right_arr, asc):
    result = []
    left_idx = 0
    right_idx = 0
    
    while left_idx < len(left_arr) and right_idx < len(right_arr):

        # if ascending is True or 1 
        if (asc == 1):    
            if left_arr[left_idx] <= right_arr[right_idx]:
                result.append(left_arr[left_idx])
                left_idx += 1
            else:
                result.append(right_arr[right_idx])
                right_idx += 1
        
        # if ascending is False or any other than 1, hence descending
        else:
            if left_arr[left_idx] >= right_arr[right_idx]:
                result.append(left_arr[left_idx])
                left_idx += 1
            else:
                result.append(right_arr[right_idx])
                right_idx += 1

    if left_idx < len(left_arr):
        result.extend(left_arr[left_idx:])
    if right_idx < len(right_arr):
        result.extend(right_arr[right_idx:])
        
    return result

# find distance between 2 points
def euclideanDistance(a,b):
    dimension=len(a)
    temp=0
    for i in range (dimension):
        temp += (a[i]-b[i])*(a[i]-b[i])
    return sqrt(temp)



'''
# Testing
# points (array of [x, y, z]) would be sorted according to x first (first element)
points3D = [[2, 3.4, -5.02], [-9, -2.54, 0], [6, 6, 6], [9, 4.7, 0.2631], [9.23, 0.3, 7.3], [2, 4, 1], [7, 2, 3]]
arr = [2.3, 3, 4.5, 2, 5, 1.5, -99.0, 203.000, -4323.000001, -2]
# arr = ['a', 's', 'n', 'g', 'l', 'r', 'u', 'c', 'b']
print(mergeSort(points3D, True))
print(mergeSort(arr, 1))
print(mergeSort(points3D))
print(mergeSort(arr, False))
print(mergeSort(points3D, 3))
'''

# Create a 3D scatter plot of the points
def scatterplot(x, y, z, colors):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter(x, y, z, c=colors, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

def visualize3D(points, closest_pair):
    x = np.array([p[0] for p in points])
    y = np.array([p[1] for p in points])
    z = np.array([p[2] for p in points])

    closest_pair_x1 = closest_pair[0][0]
    closest_pair_x2 = closest_pair[1][0]
    closest_pair_y1 = closest_pair[0][1]
    closest_pair_y2 = closest_pair[1][1]
    closest_pair_z1 = closest_pair[0][2]
    closest_pair_z2 = closest_pair[1][2]

    highlight = (x == closest_pair_x1) & (y == closest_pair_y1) & (z == closest_pair_z1) | (x == closest_pair_x2) & (y == closest_pair_y2) & (z == closest_pair_z2)
    colors = np.where(highlight, 'r', 'b')

    scatterplot(x, y, z, colors)

def visualize2D(points, closest_pair):
    x = np.array([p[0] for p in points])
    y = np.array([p[1] for p in points])
    z = np.array([0 for p in points])

    closest_pair_x1 = closest_pair[0][0]
    closest_pair_x2 = closest_pair[1][0]
    closest_pair_y1 = closest_pair[0][1]
    closest_pair_y2 = closest_pair[1][1]

    highlight = (x == closest_pair_x1) & (y == closest_pair_y1) | (x == closest_pair_x2) & (y == closest_pair_y2)
    colors = np.where(highlight, 'r', 'b')

    scatterplot(x, y, z, colors)


def visualize1D(points, closest_pair):
    x = np.array([p[0] for p in points])
    y = np.array([0 for p in points])
    z = np.array([0 for p in points])

    closest_pair_x1 = closest_pair[0][0]
    closest_pair_x2 = closest_pair[1][0]

    highlight = (x == closest_pair_x1) | (x == closest_pair_x2)
    colors = np.where(highlight, 'r', 'b')

    scatterplot(x, y, z, colors)