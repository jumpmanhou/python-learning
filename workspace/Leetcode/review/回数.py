# -*- coding: utf-8 -*-
#判断一个数是不是回数

def isPalindrome1(x):
    if(x <0 or x !=0 and x%10 ==0):
        return False
    half =0
    while(x>half):
        half = half*10 + x%10
        x = x/10
        
    return (half ==x or x==half/10)


# print(isPalindrome1(12344321))

# 判断一字符串是不是回文字符串，不考虑标点及大小写。

def isPlindrome2(s):
    
    l ,r = 0,len(s)-1
    
    while l<r:
        while l<r and not s[l].isalnum():
            l +=1
        while l<r and not s[r].isalnum():
            r -=1
            
        if s[l].lower()!=s[r].lower():
            return False
        l +=1
        r -=1
    return True
def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        ss = [c for c in s if c.isalnum()]
        
        return ''.join(ss).lower() == ''.join(ss)[::-1].lower()


print (isPalindrome("12344321"))
    
    
    
    
    
    
    
    
    
    
    