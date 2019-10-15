# 插入排序 稳定排序 原地排序 时间复杂度(介于N到N平方之间) 空间复杂度（1）
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
    i = 1
    N = len(a)
    while i < N:
        j=i
        while j > 0:
            if compareTo(a[j],a[j-1]):
                swap(a,j,j-1)
            else:
                break
            j=j-1
        i = i+1
list=[2,1,6,5,5,3,8,9,5,7,0]
sort(list)
print(list)
