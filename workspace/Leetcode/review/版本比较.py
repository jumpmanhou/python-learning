# -*-coding: utf-8 -*-
# 比较两个版本号的大小，如果是a>b，返回1，a<b 返回-1，否则0 
#把两个版本号都用列表表示，短的列表用0补齐，然后直接比较两个列表即可。


def compareVersion(version1, version2):
    v1 = map(int, version1.split('.'))
    v2 = map(int, version2.split('.'))
    v1 += [0] * (len(v2)-len(v1))
    v2 += [0] * (len(v1)-len(v2))
    if v1 > v2:
        return 1
    if v1 < v2:
        return -1
    return 0


print (compareVersion("17.16.5", "17.1"))