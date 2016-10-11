'''
Created on 2016-9-21

@author: Apprentice
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            dic[tuple(sorted(s))] = dic.get(tuple(sorted(s)),[]) + [s]
        return [item for item in dic.values()]
    
    
if __name__ == "__main__":
    strs = "eat", "tea", "tan", "ate", "nat", "bat"
    s = Solution()
    
    print(s.groupAnagrams(strs))
