'''
Created on 2016-7-24

@author: 37942
'''
'''
w tells the number of ways
v tells the previous number of ways
d is the current digit
p is the previous digit

'''
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        #dp[i] = dp[i-1] if s[i] != "0"
        #       +dp[i-2] if "09" < s[i-1:i+1] < "27"
        if s == "": return 0
        dp = [0 for x in range(len(s)+1)]
        dp[0] = 1
        fo r i in range(1, len(s)+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":  #"01"ways = 0
                dp[i] += dp[i-2]
        return dp[len(s)]
    
s = Solution()

print(s.numDecodings("1202123"))

#def numDecodings(s):
#    v, w, p = 0, int(s>''), ''
#    for d in s:
#        v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
#    return w
#
#
#print(numDecodings("1202123"))