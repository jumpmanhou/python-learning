'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility) 
P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows: 
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
from pipes import stepkinds


class Solution(object):
    def convert(self, s, nRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if nRows ==1 or len(s)<nRows:
            return s
        
        row ,step = 0,1
        
        zigzag = ['' for x in range(nRows)]
        
        for c in s:
            zigzag[row]+=c
            if row == 0:
                step =1
            elif row == nRows -1:
                step = -1
                
            row += step
        return ''.join(zigzag)
    
    
s = Solution()

print(s.convert('PAYPALISHIRING', 3))