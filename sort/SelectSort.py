# 选择排序 不稳定 原地 时间复杂度（N的平方）空间复杂度（1）
def swap(a,i,j):
        t = a[i]
        a[i]=a[j]
        a[j]=t
def compareTo(v,w):
    if(v<w):
        return True
    else:
        return False
def sort(a):
    i=0
    length = len(a)
    while i < length :
        min = i
        j = i+1
        while j < length:
            if compareTo(a[j],a[min]):
                min=j
            j=j+1   
        if min != i :
            swap(a,i,min)
        i = i+1    
list=[2,1,6,5,5,3,8,9,5,7,0]
sort(list)
print(list)
