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
#
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if nRows==1:
            return s
        period= 2*(nRows -1)
        lines=["" for i in range(nRows)]
        d={} # dict remainder:line
        for i in xrange(period):
            if i<nRows:
                d[i]=i
            else:
                d[i]=period-i
    
        for i in xrange(len(s)):
            lines[ d[i%period] ] +=s[i]
    
        return "".join(lines)