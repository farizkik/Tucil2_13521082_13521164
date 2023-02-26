from math import *

points2d = [[1,2],[3,5],[7,8],[6,8],[5,3],[4,3],[7,5],[9,3],[6,2],[7,4]]
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

# find pairs in 2D which are at most sigma distance apart
def pairSearch2D(points,sigma):
    N=len(points)
    basedimension=len(points[0])
    gap=basedimension-2
    
    # base case
    if N==1:
        return []
    if N==2:
        if euclideanDistance(points[0][gap:],points[1][gap:])<=sigma:
            return [[points[0],points[1]]]
        
    
    # if N>2, Divide and Conquer
    nearPair=[]
    
    # sort by y
    points.sort(key= lambda x:(x[gap]))
    
    # get midpoint
    y0= points[N//2][gap]
    
    # divide points to 2
    leftpoints=points[:N//2]
    rightpoints=points[N//2:]
    
    # get nearPairs from both left and right points
    nearPairLeft=pairSearch2D(leftpoints,sigma)
    nearPairRight=pairSearch2D(rightpoints,sigma)
    
    # insert to nearPair
    if not nearPairLeft:
        for pairs in nearPairLeft:
            nearPair.append(pairs)
    if not nearPairRight:
        for pairs in nearPairRight:
            nearPair.append(pairs)
    
    # construct the "strip" of d equals sigma
    strip=[]
    for p in leftpoints:
        if abs(p[gap]-y0)<=sigma:
            strip.append(p)
    for p in rightpoints:
        if abs(p[gap]-y0)<=sigma:
            strip.append(p)
            
    # sort the strip points by z
    strip.sort(key= lambda x:(x[gap+1]))
    Nstsrip=len(strip)
    
    # find ans
    for i in range(Nstsrip):
        for j in range(i+1,Nstsrip):
            # sparsity condition, 
            # don't care if y distance exceed sigma
            if strip[j][gap]-strip[i][gap]>sigma:
                break
            if euclideanDistance(strip[i][gap:],strip[j][gap:])<=sigma:
                nearPair.append([strip[i],strip[j]])
    
    # done, return nearPair
    return nearPair

def closestPair3D(points):
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
    d1=closestPair3D(leftpoints)
    d2=closestPair3D(rightpoints)
    
    # get closest dist out of the two
    d=min(d1,d2)
    
    # construct the "strip" 
    # (eh tapi kalo 3d mah bukan strip yak tapi slab)
    # gapapa deggh
    strip=[]
    for p in leftpoints:
        if abs(p[0]-x0)<=d:
            strip.append(p)
    for p in rightpoints:
        if abs(p[0]-x0)<=d:
            strip.append(p)
            
    # get the strip, now we call closestPair2D
    # BUT instead of closest pairs, 
    # we need pairs whose projections are less than d apart
    # it can be shown there are only at most O(n) numbers of these pairs
    # (we can modify the closestPair2D function to have 2 modes)
    # or just.. create new function altogether (pairSearch2D)
    minDist=d
    nearPairs=pairSearch2D(strip,d)
    for pairs in nearPairs:
        minDist=min(minDist, euclideanDistance(pairs[0],pairs[1]))
    
    # done, return minimum distance
    return minDist

# find pairs in nD which are at most sigma distance apart
def pairSearchnD(points,sigma, dimension):
    N=len(points)
    basedimension=len(points[0])
    gap=basedimension-dimension
    
    # base case
    if dimension==2:
        return pairSearch2D(points,sigma)
    if N==1:
        return 0
    if N==2:
        if euclideanDistance(points[0][gap:],points[1][gap:])<=sigma:
            return [[points[0],points[1]]]
        
    
    # if N>2, Divide and Conquer
    nearPair=[]
    
    # sort by gap
    points.sort(key= lambda x:(x[gap]))
    
    # get midpoint
    mid= points[N//2][gap]
    
    # divide points to 2
    leftpoints=points[:N//2]
    rightpoints=points[N//2:]
    
    # get nearPairs from both left and right points
    nearPairLeft=pairSearch2D(leftpoints,sigma)
    nearPairRight=pairSearch2D(rightpoints,sigma)
    
    # insert to nearPair
    if nearPairLeft!=0:
        for pairs in nearPairLeft:
            nearPair.append(pairs)
    if nearPairRight!=0:
        for pairs in nearPairRight:
            nearPair.append(pairs)
    
    # construct the "strip" of d equals sigma
    strip=[]
    for p in leftpoints:
        if abs(p[gap]-mid)<=sigma:
            strip.append(p)
    for p in rightpoints:
        if abs(p[gap]-mid)<=sigma:
            strip.append(p)
            
    nearPairProjection=pairSearchnD(strip,sigma,dimension-1)
    for pairs in nearPairProjection:
        if euclideanDistance(pairs[0][gap:],pairs[1][gap:])<=sigma:
            nearPair.append(pairs)
    # done, return nearPair
    return nearPair


def closestPairnD(points):
    N=len(points)
    dimension=len(points[0])
    
    # base case
    if dimension==2:
        return closestPair2D(points)
    if N==1:
        return inf
    if N==2:
        return euclideanDistance(points[0],points[1])
    
    # if N>2, Divide and Conquer
    
    # sort by x
    points.sort()
    
    # get midpoint
    x0= points[N//2][0]
    
    # divide points to 2
    leftpoints=points[:N//2]
    rightpoints=points[N//2:]
    
    # get closest dist in both sets of points, separately
    d1=closestPair3D(leftpoints)
    d2=closestPair3D(rightpoints)
    
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
            
    # get the strip, now we call pairSearchnD for lower dimension
    minDist=d
    nearPairs=pairSearchnD(strip,d,dimension-1)
    for pairs in nearPairs:
        minDist=min(minDist, euclideanDistance(pairs[0],pairs[1]))
    
    # done, return minimum distance
    return minDist

print(closestPairnD(points3d))
