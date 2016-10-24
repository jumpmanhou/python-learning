# -*- coding: utf-8 -*-
# 给一个没有点号的ip地址，求出所有可能的ip

def IpAddress(s):
    res = []
    len_s = len(s)
    
    for i in [1,2,3]:
        for j in [i+1,i+2,i+3]:
            for k in [j+1,j+2,j+3]:
                if k >=len_s:
                    continue
                s1 = s[:i]
                s2 = s[i:j]
                s3 = s[j:k]
                s4 = s[K:]
                if check_valid([s1,s2,s3,s4]):
                    ipAdress = s1+'.'+s2+'.'+s3+'.'+s4
                    res.append(ipAdress)
    return res

def check_valid(ls):
    for s in ls:
        if s[0]==0 and s != 0:
            return False
        if int(s)>255:
            return False
        
    return True

