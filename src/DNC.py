from utilities import *

# Make strip given conditions
def stripMake(leftpoints,rightpoints,mid,sigma,gap=0):
    leftstrip=[]
    rightstrip=[]
    
    for p in leftpoints:
        if abs(p[gap]-mid)<=sigma:
            leftstrip.append(p)
    for p in rightpoints:
        if abs(p[gap]-mid)<=sigma:
            rightstrip.append(p)
            
    leftstrip=mergeSort(leftstrip, 1,1)
    rightstrip=mergeSort(rightstrip, 1,1)
    return leftstrip,rightstrip

# divide points to left and right
def divide(points,gap=0):
    N=len(points)
    
    # sort points
    points=mergeSort(points,1,gap)
    
    # get midpoint
    midpoint= points[N//2][gap]
    
    # divide points to 2
    leftpoints=points[:N//2]
    rightpoints=points[N//2:]
    
    return leftpoints,rightpoints,midpoint

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
    
# closest pair function
def closestPairnD(points):
    N=len(points)
    dimension=len(points[0])
    
    # base case
    if dimension==1:
        return closestPair1D(points)
    if N==1:
        return [inf,None,0]
    if N==2:
        return [euclideanDistance(points[0],points[1]),[points[0],points[1]],1]
    
    # if N>2, Divide and Conquer
    
    # split points to 2
    leftpoints,rightpoints,x0=divide(points)
    
    # get closest dist in both sets of points, separately
    n_euclidean_computing=0
    d1=closestPairnD(leftpoints)
    d2=closestPairnD(rightpoints)
    
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
    
    #create strip
    leftstrip,rightstrip=stripMake(leftpoints,rightpoints,x0,d)
    
    # find ans
    minDist=d
    leftNstrip=len(leftstrip)
    rightNstrip=len(rightstrip)
    
    for i in range(leftNstrip):
        for j in range(rightNstrip):
            # sparsity condition, 
            # don't care if y distance exceed d
            if rightstrip[j][1]-leftstrip[i][1]<-d:
                continue
            if rightstrip[j][1]-leftstrip[i][1]>d:
                break
            temp=euclideanDistance(leftstrip[i],rightstrip[j])
            n_euclidean_computing+=1
            if temp<minDist:
                minDist=temp
                closestPair=[leftstrip[i],rightstrip[j]]
    
    # done, return minimum distance
    return [minDist,closestPair,n_euclidean_computing]