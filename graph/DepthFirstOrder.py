
import Graph
import queue


class DepthFirstOrder():
    marked = {}
    preOrder=queue.Queue()
    postOrder=queue.Queue()
    reversePost=queue.LifoQueue()

    def __init__(self, g):
        for s in g.all(): 
            if s not in self.marked:
                self.dfs(g, s)

    def dfs(self, g, s):
        self.marked[s] = True
        vs = g.adj(s)
        self.preOrder.put(s)
        for v in vs:
            if v not in self.marked: 
                self.dfs(g, v)
        self.postOrder.put(s)
        self.reversePost.put(s)

    def pre(self):
        return self.preOrder
    def post(self):
        return self.postOrder
    def rePost(self):
        return self.reversePost
    
