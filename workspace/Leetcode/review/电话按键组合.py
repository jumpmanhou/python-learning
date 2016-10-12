# -*- coding:utf-8 -*-
# 手机９键依次对应字幕，随机按键，请写出所有可能的字母组合。

# 典型的深度优先算法。

def letterCombian(digits):
    if not digits:
        return 
    
    dic = {"1":None,"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],
            "5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],
            "8":["t","u","v"],"9":["w","x","y","z"]}
    
    res = []
    
    dfs(dic,digits,0,'',res)
    return res

def dfs(dic,strings,index,path,res):
    if index == len(strings):
        res.append(path)
        return
    for i in dic[strings[index]]:
        dfs(dic,strings,index+1, path+i,res)
        
        
print(letterCombian("234"))
        