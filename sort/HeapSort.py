# 堆排序 非稳定排序  原地排序   时间复杂度 O(NlgN)空间复杂度O(1)
def swap(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t


def compareTo(v, w):
    if(v < w):
        return True
    else:
        return False


def swim(k):
    p = int(k/2)
    while(k > 1):
        if(compareTo(pq[p], pq[k])):
            swap(a, k, p)
            k = p
        else:
            break


def sink(k, pq):
    sinkN(k, pq, len(pq)-1)


def sinkN(k, pq, N):
    while(2*k <= N):
        j = 2*k
        if(j < N and compareTo(pq[j], pq[j+1])):
            j = j+1
        if(compareTo(pq[k], pq[j])):
            swap(pq, k, j)
            k = j
        else:
            break


def sort(a):
    N=len(a)-1
    k = int(N/2)
    while(k >= 1):
        sink(k, a)
        k = k-1
    while(N > 1):
        swap(a, 1, N)
        N = N-1
        sinkN(1, a, N)


list = [2, 1, 6, 5, 5, 3, 8, 9, 5, 7, 0, 4, 3, 2]
#list = [1, 2, 3, 5, 5, 6, 8, 5, 9, 0, 7, 4, 3, 2]
#sort(list, 0, len(list)-1)
sort(list)
print(list)
