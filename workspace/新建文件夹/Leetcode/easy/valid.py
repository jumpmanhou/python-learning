class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2!=0:
            return False
        ls =list(s)
#        dic={'()':1,'[]':2,'{}':3}
        i=0
        while len(ls)>=2:
            if ls[i]+ls[i+1] in['()','[]','{}']:
                del ls[i],ls[i]

                i=0
            else:
                i+=1
                if i>=len(ls)-1:
                    break
        if len(ls)>=2: return False
        else: return True   
 
if __name__ == "__main__":        
    s = Solution()
    a =s.isValid('[][][{}]()()()()')
    print (a)         
                          