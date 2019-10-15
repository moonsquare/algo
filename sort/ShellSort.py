# 希尔排序 不稳定 原地排序 时间复杂度（未知 大概NlgN）空间复杂度（1）
def swap(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t


def compareTo(v, w):
    if(v < w):
        return True
    else:
        return False


def sort(a):
    N = len(a)
    h = 1
    while(h < int(N/3)):
        h = 3*h+1
    while h >= 1:
        i = h
        while i < N:
            j = i
            while j > 0:
                if compareTo(a[j], a[j-h]):
                    swap(a, j, j-h)
                else:
                    break
                j = j-h
            i = i+1
        h = int(h/3)


list = [2, 1, 6, 5, 5, 3, 8, 9, 5, 7, 0, 4, 3, 2]
sort(list)
print(list)
