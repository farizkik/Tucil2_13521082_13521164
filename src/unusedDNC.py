# Theoretically has a better worst-case scenario than the one in DNC.py
# however, it does worse in average test-cases
# hence, it is not used in the final program.

from DNC import *

def pairSearch(points,sigma):
    N=len(points)
    basedimension=len(points[0])
    gap=basedimension-2
    
    # base case
    if N==1:
        return [0,0]
    if N==2:
        temp=euclideanDistance(points[0],points[1])
        if temp<=sigma:
            return [[[points[0],points[1],temp]],1]
        return [0,1]
        
    
    # if N>2, Divide and Conquer
    nearPair=[]
    
    # split points to 2
    leftpoints,rightpoints,y0=splitPoints(points,gap)
    
    # get nearPairs from both left and right points
    nearPairLeft=pairSearch(leftpoints,sigma)
    nearPairRight=pairSearch(rightpoints,sigma)
    n_euclidean_computing = nearPairLeft[1]+nearPairRight[1]
    
    # insert to nearPair
    if nearPairLeft[0]!=0:
        for pairs in nearPairLeft[0]:
            nearPair.append(pairs)
    if nearPairRight[0]!=0:
        for pairs in nearPairRight[0]:
            nearPair.append(pairs)
            
    leftstrip,rightstrip=stripMake(leftpoints,rightpoints,y0,sigma,gap)
            
    leftNstrip=len(leftstrip)
    rightNstrip=len(rightstrip)
    
    for i in range(leftNstrip):
        for j in range(rightNstrip):
            # sparsity condition, 
            # don't care if y distance exceed sigma
            if rightstrip[j][gap]-leftstrip[i][gap]<-sigma:
                continue
            if rightstrip[j][gap]-leftstrip[i][gap]>sigma:
                break
            temp=euclideanDistance(leftstrip[i],rightstrip[j])
            n_euclidean_computing+=1
            if temp<sigma:
                nearPair.append([leftstrip[i],rightstrip[j],temp])
                
    # done, return nearPair
    return [nearPair,n_euclidean_computing]

def closestPairnD(points):
    N=len(points)
    dimension=len(points[0])
    
    # base case
    if dimension==1:
        return closestPair1D(points)
    if N==1:
        return [inf,None,0]
    if N==2:
        return [euclideanDistance(points[0],points[1]), [points[0],points[1]],1]
    
    # if N>2, Divide and Conquer
    
    # split points to left and right
    leftpoints,rightpoints,x0=splitPoints(points)
    
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
    
    # construct the strip
    strip=[]
    for p in leftpoints:
        if abs(p[0]-x0)<=d:
            strip.append(p)
    for p in rightpoints:
        if abs(p[0]-x0)<=d:
            strip.append(p)
            
    # get the strip, now we call pairSearchnD for lower dimension
    minDist=d
    nearPairs=pairSearch(strip,d)
    n_euclidean_computing += nearPairs[1]
    
    if nearPairs[0]!=0:
        for pairs in nearPairs[0]:
            if pairs[2]<minDist:
                minDist=pairs[2]
                closestPair=[pairs[0],pairs[1]]
                
    # done, return minimum distance
    return [minDist,closestPair,n_euclidean_computing]
