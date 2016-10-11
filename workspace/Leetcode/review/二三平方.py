#determine n is the power of 2 or 3

def powerOfTree(n):
    return n>0 == 3**19%n

def powerOfTwo(n):
    return n>0 == 2**32%n

def powerOfFour(n):
    while n>0 and n%4==0:
        n /= 4
        
    return n ==1 

