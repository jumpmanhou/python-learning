class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack, max_area = [], 0
        for i,h in enumerate(heights):
            width = 1
            while stack and h <= stack[-1][0]:
                p = stack.pop()
                width += p[1]
                max_area = max(max_area, p[0] * (p[1] + i - p[2] - 1))
            stack.append((h, width, i))
        return max_area
    

if __name__ == "__main__":
    s= Solution()
    print(s.largestRectangleArea([4,0,1,1]))