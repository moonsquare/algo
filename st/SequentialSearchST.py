# 基于顺序查找（无序链表）的符号表实现 时间复杂度 查找N 插入 N
class Node:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

    def printV(self):
        print(self.key)


def put(key):
    global first
    node = first
    while (node != None):
        if(key == node.key):
            node.value = key+1
            return
        node = node.next
    first = Node(key, key+1, first)


def get(key):
    node = first
    while (node != None):
        if(key == node.key):
            return node
        node = node.next
    return


first = Node(1, 2, None)

for i in range(10):
    put(i)

print(get(6).key, get(6).value)
