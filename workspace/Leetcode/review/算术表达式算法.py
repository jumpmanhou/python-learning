# -*- coding: utf-8 -*- 
# 给定一个算术表达式，在不同的地方加上括号，求所有可能的值
# 例如：‘2-1-1’ 可以得出（2-1）-1 =0 和2-（1-1） = 2，返回结果[0,2]

# 递归，依次把操作符号左右的数算出来，然后再用对应的符号把左右两部分算出来。
def diffWaysToCompute(input):
        """
        :type input: str
        :rtype: List[int]
        """
        #列表解析式
        return [a+b if c == '+' else a-b if c == '-' else a*b
            for i, c in enumerate(input) if c in '+-*'
            for a in diffWaysToCompute(input[:i])
            for b in diffWaysToCompute(input[i+1:])] or [int(input)]
            
    