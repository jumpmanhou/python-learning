'''
Created on 2016-09-21

@author: Apprentice
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # using dfs
        res = []
        if n == 0:
            return res
        self.dfs(n,n,'',res)
        return res
        
    def dfs(self,l,r,item,res):
        if l > r:
            return
        if l ==0 and r == 0:
            res.append(item)
            
        if l:
            self.dfs(l-1,r,item+'(',res)
        if r:
            self.dfs(l,r-1,item+')',res)
            
        
    
    
    
if __name__ == "__main__":
    s = Solution()
    print (s.generateParenthesis(3))