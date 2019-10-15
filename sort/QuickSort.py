#快速排序  不稳定排序 原地排序 时间复杂度（平均NlgN）空间复杂度（lgN）
def swap(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t


def compareTo(v, w):
    if(v < w):
        return True
    else:
        return False


def sort(a, lo, hi):
    if lo >= hi:
        return
    v = a[lo]
    i = lo+1
    j = hi
    while True:
        while compareTo(a[i], v):
            if i == hi:
                break
            i = i+1
        while compareTo(v, a[j]):
            if j == lo:
                break
            j = j-1
        if i >= j:
            break
        swap(a, i, j)
        i = i+1
        j = j-1
    swap(a, j, lo)
    sort(a, lo, j-1)
    sort(a, j+1, hi)


list = [2, 1, 6, 5, 5, 3, 8, 9, 5, 7, 0, 4, 3, 2]
sort(list, 0, len(list)-1)
print(list)
