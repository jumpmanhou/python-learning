class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x<0 or x>2**31-1:return False
        if (x!=0 and x%10==0):
            return False
        rst = 0
        while x>rst:
            rst =rst*10+x%10
            x //=10
            
        return (x==rst) or (x==rst//10)
    
if __name__ == "__main__":        
    s = Solution()
    a =s.isPalindrome(10)
    print (a)         
    