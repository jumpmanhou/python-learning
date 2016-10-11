# -*- coding: utf-8 -*-
# 1.只能交易一次，保证获利最大。

def maxprofit1(prices):
    if not prices:
        return 0
    profit = 0
    minprice =prices[0]
    for p in prices[1:]:
        minprice = min(p,minprice)
        profit = max(p-minprice,profit)
        
    return profit if profit>0 else 0


print (maxprofit1([7,4,2,3,5,6]))

# 能不限次数交易，但是买之前必须先卖掉。 只要后一天比今天的价格贵，今天就买，明天卖掉。

def maxprofit2(prices):
    return sum(max(prices[i+1]-prices[i],0) for i in range(len(prices)-1))

print (maxprofit2([1,2,3,4,5,6,7]))


