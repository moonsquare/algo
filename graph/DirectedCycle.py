# 有向环

import queue
import Graph


class DirectedCycle:
    marked = {}
    edgeTo = {}
    cycles = queue.LifoQueue()  # 有向环的顶点
    onStack = {}  # 递归调用栈上的所有顶点

    def __init__(self, g):
        for i in range(12):
            if i not in self.marked:
                self.dfs(g, i)

    def dfs(self, g, v):
        self.onStack[v] = True
        self.marked[v] = True
        ws = g.adj(v)
        for w in ws:
            if(self.hasCycle() == True):
                return
            elif w not in self.marked:
                self.edgeTo[w] = v
                self.dfs(g, w)
            elif(self.onStack[w]):
                x = v
                while(x != w):
                    self.cycles.put(x)
                    x = self.edgeTo[x]
                self.cycles.put(w)
                self.cycles.put(v)
        self.onStack[v] = False

    def hasCycle(self):  # 是否有环
        return self.cycles.empty()==False

    def cycle(self):  # 环上的所有顶点
        return self.cycles
