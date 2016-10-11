'''
Created on 2016-7-4

@author: 37942
'''
import functools
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return functools.reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])

s = Solution()
digits = '23'
print (s.letterCombinations(digits))