# uglyNumber contain factor only in [2,3,5]

def isUgly(num):
    for i in [2,3,5]:
            while num%i==0 <num:
                num = num/i
                
    return num ==1


print (isUgly(84))