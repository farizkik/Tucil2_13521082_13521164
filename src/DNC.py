from utilities import *
points2d = [[1,2],[3,5],[7,8],[6,8],[5,3],[4,3],[7,5],[9,3],[6,2],[7,4]]
points3d = [[1,2,3],[4,5,6],[2,3,4],[3,5,6],[7,8,9]]

# remember to:
# improve algo by changing sorting place (sort first before splicing)
# change sort to custom made sort

# find pairs in 2D which are at most sigma distance apart
def pairSearch2D(points,sigma):
    N=len(points)
    basedimension=len(points[0])
    gap=basedimension-2
    
    # base case
    if N==1:
        return [0,0]
    if N==2:
        if euclideanDistance(points[0][gap:],points[1][gap:])<=sigma:
            return [[[points[0],points[1]]],1]
        return [0,0]
        
    
    # if N>2, Divide and Conquer
    nearPair=[]
    
    # sort by y
    #points.sort(key= lambda x:(x[gap]))
    points=mergeSort(points,1,gap)
    
    # get midpoint
    y0= points[N//2][gap]
    
    # divide points to 2
    leftpoints=points[:N//2]
    rightpoints=points[N//2:]
    
    # get nearPairs from both left and right points
    nearPairLeft=pairSearch2D(leftpoints,sigma)
    nearPairRight=pairSearch2D(rightpoints,sigma)
    n_euclidean_computing = nearPairLeft[1]+nearPairRight[1]
    
    # insert to nearPair
    if nearPairLeft[0]!=0:
        for pairs in nearPairLeft[0]:
            nearPair.append(pairs)
    if nearPairRight[0]!=0:
        for pairs in nearPairRight[0]:
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
    #strip.sort(key= lambda x:(x[gap+1]))
    strip=mergeSort(strip,1,gap+1)
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
            n_euclidean_computing+=1
    
    # done, return nearPair
    return [nearPair,n_euclidean_computing]

# find pairs in nD which are at most sigma distance apart
def pairSearchnD(points,sigma, dimension):
    N=len(points)
    basedimension=len(points[0])
    gap=basedimension-dimension
    
    # base case
    if dimension==2:
        return pairSearch2D(points,sigma)
    if N==1:
        return [0,0]
    if N==2:
        if euclideanDistance(points[0][gap:],points[1][gap:])<=sigma:
            return [[[points[0],points[1]]],1]
        return [0,1]
        
    # if N>2, Divide and Conquer
    nearPair=[]
    
    # sort by gap
    #points.sort(key= lambda x:(x[gap]))
    points=mergeSort(points,1,gap)
    
    # get midpoint
    mid= points[N//2][gap]
    
    # divide points to 2
    leftpoints=points[:N//2]
    rightpoints=points[N//2:]
    
    # get nearPairs from both left and right points
    nearPairLeft=pairSearchnD(leftpoints,sigma,dimension)
    nearPairRight=pairSearchnD(rightpoints,sigma,dimension)
    
    n_euclidean_computing= nearPairLeft[1]+nearPairRight[1]
    
    # insert to nearPair
    if nearPairLeft[0]!=0:
        for pairs in nearPairLeft[0]:
            nearPair.append(pairs)
    if nearPairRight[0]!=0:
        for pairs in nearPairRight[0]:
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
    if nearPairProjection[0]!=0:
        for pairs in nearPairProjection[0]:
            if euclideanDistance(pairs[0][gap:],pairs[1][gap:])<=sigma:
                nearPair.append(pairs)
            n_euclidean_computing+=1
    # done, return nearPair
    return [nearPair,n_euclidean_computing]

# closest pair in 1d
def closestPair1D(points):
    N=len(points)
    points=mergeSort(points,1)
    minDist=inf
    closestPair=None
    n_euclidean_computing=0
    for i in range(N-1):
        distance=euclideanDistance(points[i],points[i+1])
        n_euclidean_computing+=1
        if distance<minDist:
            minDist=distance
            closestPair=[points[i],points[i+1]]
    return[minDist,closestPair,n_euclidean_computing]
    
        
    

# closest pair in 2d
def closestPair2D(points):
    N=len(points)
    
    # base case
    if N==1:
        return [inf,None,0]
    if N==2:
        return [euclideanDistance(points[0],points[1]),[points[0],points[1]],1]
    
    # if N>2, Divide and Conquer
    
    # sort by x
    #points.sort()
    points=mergeSort(points)
    
    # get midpoint
    x0= points[N//2][0]
    
    # divide x to 2
    leftpoints=points[:N//2]
    rightpoints=points[N//2:]
    
    # get closest dist in both sets of points, separately
    n_euclidean_computing=0
    d1=closestPair2D(leftpoints)
    d2=closestPair2D(rightpoints)
    
    n_euclidean_computing = d1[2]+d2[2]
    
    # get closest dist out of the two
    closestPair=None
    d=inf
    if(d1[0]<d2[0]):
        d=d1[0]
        closestPair=d1[1]
    else:
        d=d2[0]
        closestPair=d2[1]
    
    # construct the "strip"
    strip=[]
    for p in leftpoints:
        if abs(p[0]-x0)<=d:
            strip.append(p)
    for p in rightpoints:
        if abs(p[0]-x0)<=d:
            strip.append(p)
            
    # sort the strip points by y
    
    #strip.sort(key= lambda x:(x[1],x[0]))
    strip=mergeSort(strip, 1,1)
    Nstsrip=len(strip)
    
    # find ans
    minDist=d
    for i in range(Nstsrip):
        for j in range(i+1,Nstsrip):
            # sparsity condition, 
            # don't care if y distance exceed d
            if strip[j][1]-strip[i][1]>d:
                break
            temp=euclideanDistance(strip[i],strip[j])
            n_euclidean_computing+=1
            if temp<minDist:
                minDist=temp
                closestPair=[strip[i],strip[j]]
    
    # done, return minimum distance
    return [minDist,closestPair,n_euclidean_computing]


def closestPairnD(points):
    N=len(points)
    dimension=len(points[0])
    
    # base case
    if dimension==1:
        return closestPair1D(points)
    if dimension==2:
        return closestPair2D(points)
    if N==1:
        return [inf,None,0]
    if N==2:
        return [euclideanDistance(points[0],points[1]), [points[0],points[1]],1]
    
    # if N>2, Divide and Conquer
    
    # sort by x
    #points.sort()
    points=mergeSort(points)
    
    # get midpoint
    x0= points[N//2][0]
    
    # divide points to 2
    leftpoints=points[:N//2]
    rightpoints=points[N//2:]
    
    
    # get closest dist in both sets of points, separately
    d1=closestPairnD(leftpoints)
    d2=closestPairnD(rightpoints)
    closestPair=None
    n_euclidean_computing = d1[2]+d2[2]
    
    # get closest dist out of the two
    d=inf
    if(d1[0]<d2[0]):
        d=d1[0]
        closestPair=d1[1]
    else:
        d=d2[0]
        closestPair=d2[1]
    
    
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
    n_euclidean_computing += nearPairs[1]
    if nearPairs[0]!=0:
        for pairs in nearPairs[0]:
            temp=euclideanDistance(pairs[0],pairs[1])
            n_euclidean_computing += 1
            if temp<minDist:
                minDist=temp
                closestPair=pairs
    
    # done, return minimum distance
    return [minDist,closestPair,n_euclidean_computing]


'''
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
'''