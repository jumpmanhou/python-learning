'''
Created on 2016-7-10

@author: 37942
'''
import collections
class Solution(object):
    def anagrams(self, strs):
        count = collections.Counter([tuple(sorted(s)) for s in strs])
        return filter(lambda x: count[tuple(sorted(x))]>1, strs)
s = Solution()

print(s.anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))