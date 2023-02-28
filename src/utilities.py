from math import *
import matplotlib.pyplot as plt
import numpy as np

# Merge Sort Algorithm Using Divide and Conquer Approach for Array of Points
# in default, sorting would be ascending
def mergeSort(arr, asc = 1, el=0):
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    left_arr = mergeSort(left_arr, asc, el)
    right_arr = mergeSort(right_arr, asc, el)

    # conquer
    return merge(left_arr, right_arr, asc, el)


# conquer implementation
def merge(left_arr, right_arr, asc,el):
    result = []
    left_idx = 0
    right_idx = 0
    
    while left_idx < len(left_arr) and right_idx < len(right_arr):

        # if ascending is True or 1 
        if (asc == 1):    
            if left_arr[left_idx][el] <= right_arr[right_idx][el]:
                result.append(left_arr[left_idx])
                left_idx += 1
            else:
                result.append(right_arr[right_idx])
                right_idx += 1
        
        # if ascending is False or any other than 1, hence descending
        else:
            if left_arr[left_idx][el] >= right_arr[right_idx][el]:
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

# Create a 3D scatter plot of the points
def visualize3D(points, closest_pair_list):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    for i in range(len(points)):
        flag = False
        for j in range(len(closest_pair_list)):
            if points[i] in closest_pair_list[j]:
                flag = True
        if not flag:
            ax.scatter(points[i][0], points[i][1], points[i][2], c='b')
        else:
            ax.scatter(points[i][0], points[i][1], points[i][2], c='r')

    for i in range(len(closest_pair_list)):
        x = [closest_pair_list[i][0][0], closest_pair_list[i][1][0]]
        y = [closest_pair_list[i][0][1], closest_pair_list[i][1][1]]
        z = [closest_pair_list[i][0][2], closest_pair_list[i][1][2]]
        ax.plot(x, y, z, c='r')
    plt.show()

def visualize2D(points, closest_pair_list):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    for i in range(len(points)):
        flag = False
        for j in range(len(closest_pair_list)):
            if points[i] in closest_pair_list[j]:
                flag = True
        if not flag:
            ax.scatter(points[i][0], points[i][1], c='b')
        else:
            ax.scatter(points[i][0], points[i][1], c='r')

    for i in range(len(closest_pair_list)):
        x = [closest_pair_list[i][0][0], closest_pair_list[i][1][0]]
        y = [closest_pair_list[i][0][1], closest_pair_list[i][1][1]]
        ax.plot(x, y, c='r')
    plt.show()

def visualize1D(points, closest_pair_list):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    for i in range(len(points)):
        flag = False
        for j in range(len(closest_pair_list)):
            if points[i] in closest_pair_list[j]:
                flag = True
        if not flag:
            ax.scatter(points[i][0], 0, 0, c='b')
        else:
            ax.scatter(points[i][0], 0, 0, c='r')

    for i in range(len(closest_pair_list)):
        x = [closest_pair_list[i][0][0], closest_pair_list[i][1][0]]
        ax.plot(x, [0, 0], [0, 0], c='r')
    plt.show()