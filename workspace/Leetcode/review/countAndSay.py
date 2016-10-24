# -*- coding : utf-8 -*-

def countAndSay(n):
    s= '1'
    for i in range(n-1):
        let, count, tmp = s[0],0,''
        
        for c in s:
            if c == let:
                count += 1
            else: 
                tmp += str(count)+let
                let = c
                count = 1
        tmp += str(count)+let    
        s= tmp 
        
    return s


print (countAndSay(5))
              
        