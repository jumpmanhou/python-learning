class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_price = 0, float("inf")
        
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit
    
    def maxProfit2(self,prices):
        
        return sum(max(prices[i+1]-prices[i],0) for i in range(len(prices)-1))
    
    
if __name__ == "__main__":        
    s = Solution()
    a =s.maxProfit2([7,1,5,3,6,4])
    print (a)         
    a.isalnum()