'''
Created on 2016-6-30

@author: 37942
'''

class Solution(object):
    
    def longSub(self,s):
        maxLength = start = 0
        used = {}
        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:
                start = used[s[i]] +1
                
            else:
                maxLength = max(maxLength, i-start+1)
            used[s[i]]=i
                
        return maxLength
    
s = Solution()

print (s.longSub("iffawaisaffsawlffka"))
    