# -*- coding: utf-8 -*-
#给定一个正整数，如果是偶数，则n/2,如果是奇数，可以加1或者减1，求变换到1需要最少的次数。
# 递归：basecase:n=1:return 0



def integerReplace(n):
    if n==1:
        return 0
    if n%2:
        return 1+min(integerReplace(n+1),integerReplace(n-1))
    else:
        return 1+integerReplace(n/2)
    
    
print (integerReplace(16))
