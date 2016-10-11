class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==1:
            return strs[0]
        for i in range(len(strs)-1):
            prefix=''
            for j in range(min(len(strs[i]),len(strs[i+1]))):
                if strs[i][j]==strs[i+1][j]:
                    prefix = prefix+(strs[i][j])
                else:
                    strs[i+1]=prefix
                    break
        return prefix
    
if __name__ == "__main__":        
    s = Solution()
    a =s.longestCommonPrefix(['ab','abcsa','asfc'])
    print (a)         
               