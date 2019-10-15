# 归并排序 稳定排序  非原地排序   时间复杂度 O(NlgN)空间复杂度O(N)
def swap(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t


def compareTo(v, w):
    if(v < w):
        return True
    else:
        return False


def merge(a, lo, mid, hi):
    i = lo
    j = mid+1
    for k in range(lo, hi+1):
        aux[k] = a[k]
    for k in range(lo, hi+1):
        if(i > mid):
            a[k] = aux[j]
            j = j+1
        elif(j > hi):
            a[k] = aux[i]
            i = i+1
        elif(compareTo(aux[i], aux[j])):
            a[k] = aux[i]
            i = i+1
        else:
            a[k] = aux[j]
            j = j+1


def sort(a, lo, hi):
    if(hi <= lo):
        return
    mid = lo+int((hi-lo)/2)
    sort(a, lo, mid)
    sort(a, mid+1, hi)
    merge(a, lo, mid, hi)

def sortBu(a):
    N = len(a);
    i=1
    while (i<N):
        j=0
        while(j<N-i):
            merge(a,j,j+i-1,min(j+i+i-1,N-1))
            j=j+i+i
        i=i+i

list = [2, 1, 6, 5, 5, 3, 8, 9, 5, 7, 0, 4, 3, 2]
#list = [1, 2, 3, 5, 5, 6, 8, 5, 9, 0, 7, 4, 3, 2] 
aux = list.copy()
#sort(list, 0, len(list)-1)
sortBu(list)
print(list)
