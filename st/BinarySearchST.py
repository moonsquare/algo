# 基于二分查找（有序数组）的符号表，时间复杂度 查找 lgN 插入 ？

def get(key):
    lo=0
    hi=N-1
    return rank(key,lo,hi)

def rank(key,lo,hi):
    if(hi<lo):return lo 
    mid = lo+ (hi-lo)//2
    if (key = keys[mid]):
        return mid
    elif(key < keys[mid]):
        hi=mid-1
    else:
        lo=mid+1
    return rank(key,lo,hi)

def put(key,value):
    




N = len(keys)
