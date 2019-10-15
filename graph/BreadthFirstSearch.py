
import Graph
import queue

class BreadthFirstSearch():
    marked = {}
    toEdge = {}
    start = 0

    def __init__(self, g, s):
        self.dfs(g, s)
        start = s

    def dfs(self, g, s):
        q = queue.Queue()
        q.put(s)
        self.marked[s]=True
        while not q.empty():
            w=q.get()
            vs = g.adj(w)
            for v in vs:
                if v not in self.marked:
                    self.marked[v] = True
                    self.toEdge[v] = w
                    q.put(v)

    def hasPathTo(self, s):
        if s in self.marked:
            return self.marked[s]
        else:
            return False

    def pathTo(self, s):
        a = []
        if(self.hasPathTo(s) == False):
            return a
        v = s
        a.append(s)
        while(v != self.start):
            a.append(self.toEdge[v])
            v = self.toEdge[v]
        return a


g = Graph.Graph()
bfs = BreadthFirstSearch(g, 0)
print(bfs.pathTo(5))
print(bfs.pathTo(4))
