# -*- coding:utf-8 -*-
# 排序

# 冒泡排序：每回合从第一个元素开始和后面的元素比较，最大的放到最后。

def bubbleSort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    
    return lst

print (bubbleSort([2,1,3,45,5,2,1,56,23,9]))

# 选择排序：

def selectSort(lst):
    for i in range(len(lst) - 1, 0, -1):
        pos_of_max = 0
        for j in range(1, i + 1):
            if lst[j] > lst[pos_of_max]:
                pos_of_max = j
                
        lst[i],lst[pos_of_max] = lst[pos_of_max],lst[i]
                
    return lst

print (selectSort([2,1,3,45,5,2,1,56,23,9]))


# 插入排序：每次假设前面的元素都是已经排好序了的，然后将当前位置的元素插入到原来的序列中

def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
        
    return a_list

print(insertion_sort([2,1,3,45,5,2,1,56,23,9]))

# 快速排序：
def qsort(seq):
    if seq==[]:
        return []
    else:
        pivot=seq[0]
        lesser=qsort([x for x in seq[1:] if x<pivot])
        greater=qsort([x for x in seq[1:] if x>=pivot])
        return lesser+[pivot]+greater
    
print(qsort([2,1,3,45,5,2,1,56,23,9]))  
