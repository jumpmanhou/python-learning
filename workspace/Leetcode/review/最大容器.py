# -*- coding: utf-8 -*- 


def maxArea(heights):
    l,r = 0,len(heights)
    water = 0
    while l<r:
        water = max(water,(r-l)*min(heights[l],heights[r]))
        if heights[l]<heights[r]:
            l +=1
        else:
            r -=1
    return water
    
    
    
    
print (maxArea([1,2,3,5,3,5]))
    