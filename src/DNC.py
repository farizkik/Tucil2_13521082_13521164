from math import *

points2d = [[1,2],[1,2],[3,5],[7,8],[6,8],[5,3],[4,3],[7,5],[9,3],[6,2],[7,4]]
points3d = [[1,2,3],[4,5,6],[2,3,4],[3,5,6],[7,8,9]]

# remember to:
# improve algo by changing sorting place (sort first before splicing)
# change sort to custom made sort

# find distance between 2 points
def euclideanDistance(a,b):
    dimension=len(a)
    temp=0
    for i in range (dimension):
        temp += (a[i]-b[i])*(a[i]-b[i])
    return sqrt(temp)

# closest pair in 2d
def closestPair2D(points):
    N=len(points)
    
    # base case
    if N==1:
        return inf
    if N==2:
        return euclideanDistance(points[0],points[1])
    
    # if N>2, Divide and Conquer
    
    # sort by x
    points.sort()
    
    # get midpoint
    x0= points[N//2][0]
    
    # divide x to 2
    leftpoints=points[:N//2]
    rightpoints=points[N//2:]
    
    # get closest dist in both sets of points, separately
    d1=closestPair2D(leftpoints)
    d2=closestPair2D(rightpoints)
    
    # get closest dist out of the two
    d=min(d1,d2)
    
    # construct the "strip"
    strip=[]
    for p in leftpoints:
        if abs(p[0]-x0)<=d:
            strip.append(p)
    for p in rightpoints:
        if abs(p[0]-x0)<=d:
            strip.append(p)
            
    # sort the strip points by y
    strip.sort(key= lambda x:(x[1],x[0]))
    Nstsrip=len(strip)
    
    # find ans
    minDist=d
    for i in range(Nstsrip):
        for j in range(i+1,Nstsrip):
            # sparsity condition, 
            # don't care if y distance exceed d
            if strip[j][1]-strip[i][1]>d:
                break
            minDist=min(minDist,euclideanDistance(strip[i],strip[j]))
    
    # done, return minimum distance
    return minDist
                        
print(closestPair2D(points2d))
