# -*- coding: utf-8 -*-
#求小于n的素数右多少个:先定义一个数组，把所有树都当成素数，然后在把以base为因子的数都变为非素数，最后求数组的和。

def countPrimes(n):
    if n<=2:
        return 0
    
    prime =[True]*n
    prime[0]=prime[1]=False
    
    for base in range(int(n**0.5)+1):
        if prime[base]:
            prime[base**2::base] = [False]*len(prime[base**2::base])
            
    return sum(prime)


print (countPrimes(1000))
        