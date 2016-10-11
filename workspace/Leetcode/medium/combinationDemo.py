'''
Created on 2016-7-20

@author: 37942
'''

from itertools import combinations

class Solution:
    def combine1(self, n, k):
        return list(combinations(range(1, n+1), k))
    
    def combine2(self, n, k):
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(1, n+1) for pre in self.combine2(i-1, k-1)]



s = Solution()

print(s.combine1(5, 2))
print(s.combine2(5, 2))