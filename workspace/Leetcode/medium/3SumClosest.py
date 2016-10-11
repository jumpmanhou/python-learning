'''
Created on 2016-7-4

@author: 37942
'''

def threeSumClose(s,target):
    s.sort()
    he = s[0]+s[1]+s[2]
    
    for i in range(len(s)-2):
        j,k = i+1, len(s)-1
        while j < k:
            temp = s[i]+s[j]+s[k]
            if temp == target:
                return target
        
            if abs(temp - target)<abs(he - target):
                he = temp
            
            if temp < target:
                j+=1
            elif temp > target:
                k -= 1
    return he

print(threeSumClose([2,3,4,5,6,7],19))