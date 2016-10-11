'''
Created on 2016-8-23

@author: 37942
'''
'''
keynotes:

1. If car starts at A and can not reach B. Any station between A and B
 can not reach B.(B is the first station that A can not reach.)
2.If the total number of gas is bigger than the total number of cost. There must be a solution.

'''
    

class Solution(object):
    
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 0 or len(cost) == 0 or sum(gas) < sum(cost):
            return -1
        position = 0
        balance = 0 # current tank balance
        for i in range(len(gas)):
            balance += gas[i] - cost[i] # update balance
            if balance < 0: # balance drops to negative, reset the start position
                balance = 0
                position = i+1
        return position
    
    
s = Solution()

gas = [2,3,4,5,6,7]
cost = [3,2,1,5,4,6]

print(s.canCompleteCircuit(gas, cost))
