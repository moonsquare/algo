# 二叉查找树符号表 插入和查找的 时间复杂度都在 对数级别,二叉查找树的问题在于构造的时候很有可能造成树是不平衡的，那么时间复杂度就会上升到N


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def printV(self):
        print(self.key)


class BST:
    root = None

    def getByNode(self, node, key):
        if(node == None):
            return None
        elif(node.key == key):
            return node.value
        elif(key > node.key):
            return self.getByNode(node.right, key)
        elif(key < node.key):
            return self.getByNode(node.left, key)

    def putByNode(self, node, key, value):
        if(node == None):
            return Node(key, value)
        elif(key > node.key):
            node.right = self.putByNode(node.right, key, value)
        elif(key < node.key):
            node.left = self.putByNode(node.left, key, value)
        else:
            node.value = value
        return node

    def get(self, key):
        return self.getByNode(self.root, key)

    def put(self, key, value):
        self.root = self.putByNode(self.root, key, value)

    def delete(self, key):
        return self.deleteByNode(self.root, key)

    def min(self, node):
        if(node.left == None):
            return node
        else:
            return self.min(node.left)

    def deleteByNode(self, node, key):
        if(node == None):
            return None
        elif(key < node.key):
            node.left = self.deleteByNode(node.left, key)
        elif(key > node.key):
            node.right = self.deleteByNode(node.right, key)
        else:
            if(node.right == None):
                return node.left
            if(node.left == None):
                return node.right
            minNode = self.min(node.right)
            minNode.right = self.deletemin(node.right)
            minNode.left = node.left
            return minNode
        return node

    def deletemin(self, node):
        if(node.left == None):
            return node.right
        node.left = deletemin(node.left)
        return node


value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = ["a", "x", "b", "z", "y", "g", "h", "u", "p", "e"]

bst = BST()
for i in range(10):
    bst.put(key[i], value[i])
print(bst.get("u"))
bst.delete("g")
print(bst.get("e"))
bst.delete("u")
print(bst.get("b"))
