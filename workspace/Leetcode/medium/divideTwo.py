'''
Created on 2016-7-5

@author: 37942
'''

def divideTwoInteger(divident, divider):
    sign = (divident<0) is (divider<0)
    res = 0
    divident,divider  = abs(divident), abs(divider)
    
    while divident >= divider:
        i, tmp = 1, divider
        while divident>tmp:
            res +=i
            divident -= tmp
            i <<1
            tmp <<1
    return res if sign==True else -res

print(divideTwoInteger(11,2))
        