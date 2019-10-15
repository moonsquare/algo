# 基于红黑树的符号表，红黑树是一个平衡二叉树，查找和插入都是对数级别的
class Node:
    RED = True
    BLACK = False

    def __init__(self, key, value, color):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.color = color


def isRed(node):
    if(node == None):
        return False
    return node.color


class RedBlackBST:
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

    def get(self, key):
        return self.getByNode(self.root, key)

    def put(self, key, value):
        self.root = self.putByNode(self.root, key, value)
        self.root.color = Node.BLACK

    def putByNode(self, node, key, value):
        if(node == None):
            node = Node(key, value, Node.RED)
            return node
        elif(key > node.key):
            node.right = self.putByNode(node.right, key, value)
        elif(key < node.key):
            node.left = self.putByNode(node.left, key, value)
        elif(node.key == key):
            node.value = value
            return node
        if(isRed(node.left) == False and isRed(node.right)):
            node = self.rotateLeft(node)
        if(isRed(node.left) and isRed(node.left.left)):
            node = self.rotateRight(node)
        if(isRed(node.left) and isRed(node.right)):
            self.flipColors(node)
        return node

    def rotateLeft(self, node):
        right = node.right
        node.right = right.left
        right.left = node
        right.color = node.color
        node.color = Node.RED
        return right

    def rotateRight(self, node):
        left = node.left
        node.left = left.right
        left.right = node
        left.color = node.color
        node.color = Node.RED
        return left

    def flipColors(self, node):
        node.color = Node.RED
        node.left.color = Node.BLACK
        node.right.color = Node.BLACK


value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = ["a", "x", "b", "z", "y", "g", "h", "u", "p", "e"]

bst = RedBlackBST()
for i in range(10):
    bst.put(key[i], value[i])
print(bst.get("u"))
print(bst.get("e"))
print(bst.get("b"))
