import sys


class MinStack:
    def __init__(self):
        self.minStack = []
        self.minValue = sys.maxsize

    def push(self, val: int) -> None:
        if val < self.minValue:
            self.minValue = val
        self.minStack.append(val)

    def pop(self) -> None:
        if self.top() == self.minValue:
            self.minStack.pop(len(self.minStack) - 1)
            # 找出最小的元素
            if self.minStack:
                self.minValue = min(self.minStack)
            else:
                self.minValue = sys.maxsize
        else:
            self.minStack.pop(len(self.minStack) - 1)

    def top(self) -> int:
        return self.minStack[len(self.minStack) - 1]

    def getMin(self) -> int:
        return self.minValue
