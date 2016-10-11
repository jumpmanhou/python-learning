#determine a number is happy number or not 
# happy number : for example:
"""
19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

def isHappy(n):
    mem = set()
    while n!=1:
        n = sum([int(b)**2 for b in str(n)])
        if n not in mem:
            mem.add(n)
        else:
            return False
        
    return True

print (isHappy(42))
            
        
            