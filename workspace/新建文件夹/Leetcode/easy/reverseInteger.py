class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
# method 1:
#        if x > 2147483647:
#            return 0
#        rst = 0
#        pos_x = abs(x)
#        while pos_x:
#            rst = rst*10+pos_x%10
#            pos_x //= 10
#        if rst >  2147483647:
#            return 0  
#        return rst if x>0 else rst*(-1)
#method 2:
        if x<0:
            x=-1*x
            rst = int(''.join(list(str(x)[::-1])))
        else :
            rst= int(''.join(list(str(x)[::-1])))
        if rst>2147483647 or rst<-2147483647:
            return 0
        else:
            return rst
        
if __name__ == "__main__":        
    s = Solution()
    a =s.reverse(-100000236653)
    print (a)          