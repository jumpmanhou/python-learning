'''
@author: Apprentice
'''

def countBits(num):
    res = [0]*(num+1)
    
    for i in range(num+1):
        res[i] = res[i>>1] + (i&1)
        
    return res


print(countBits(10))