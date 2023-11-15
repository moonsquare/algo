class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.tail = DLinkedNode()
        self.head = DLinkedNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_to_head(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            # 更新值
            node.value = value
            # 移到头部
            self.move_to_head(node)
        elif self.size >= self.capacity:
            # 最久的节点
            remove_node = self.tail.pre
            # 移除队列
            self.remove_node(remove_node)
            # 移除缓存
            self.cache.pop(remove_node.key)

            # 放入缓存并标记最新
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.add_to_head(node)
        # 缓存还没满
        else:
            self.size += 1
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.add_to_head(node)

    def remove_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def add_to_head(self, node):
        node.pre = self.head
        node.next = self.head.next

        node.next.pre = node
        node.pre.next = node

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)
