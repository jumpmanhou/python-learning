'''
Created on 2016-9-21

@author: Apprentice
'''
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for item in path.split("/"):
            if item not in [".", "..", ""]:
                stack.append(item)
            if item == ".." and stack:
                stack.pop()
        return "/" + "/".join(stack)
    
if __name__ == "__main__":
    path = '/a/b/../a/b/a/'
    s = Solution()
    print s.simplifyPath(path)