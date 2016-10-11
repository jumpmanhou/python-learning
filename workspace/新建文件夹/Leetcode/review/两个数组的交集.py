# -*- coding: utf-8 -*-
# 1.求交集，每个元素只出现一次。2.求交集，交集中每个元素有多少返回多少。(字典记录元素与次数)


def interSect1(nums1,nums2):
    return list(set(nums1)&set(nums2))

def interSect2(nums1,nums2):
    d = {}
    res = []
    for n in nums1:
        d[n] = d.get(n,0)+1
        
    for n in nums2:
        if n in d and d[n]>0:
            res.append(n)
            d[n] -= 1
            
    return res
nums1 = [1,2,2,1]
nums2 = [2,2]

print (interSect1(nums1, nums2))
print (interSect2(nums1, nums2))

    