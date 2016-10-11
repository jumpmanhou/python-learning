# -*- coding: utf-8 -*-

#杨辉三角: 每一行等于上一行（0+【】）+（【】+0）

def generate(numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]
    
    
if __name__ == "__main__":
    print (generate(5))