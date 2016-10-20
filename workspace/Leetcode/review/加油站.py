# -*- coding: utf-8 -*- 
# 一条环形道路上油n个加油站，每个加油站可以获得gas(i)，到下一个加油站要消耗cost(i),
# 求汽车从哪个加油站除法可以绕道路行驶一圈，假设只有一个解。

# 当gas的总和比cost总和大的时候，才会有解。

def completeCircle(gas,cost):
    if len(gas)<0 or len(cost)<0 or sum(gas)<sum(cost):
        return -1
    
    balance = 0
    position = 0
    for i in range(len(cost)):
        balance += gas[i]-cost[i]
        if balance < 0:
            blance = 0
            position = i+1
            
    return position 

print (completeCircle([2,3,1,4], [1,4,3,1]))
    
    