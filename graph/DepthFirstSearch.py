
import Graph


class DepthFirstSearch():
    marked = {}
    toEdge = {}
    start = 0

    def __init__(self, g, s):
        self.dfs(g, s)
        start = s

    def dfs(self, g, s):
        self.marked[s] = True
        vs = g.adj(s)
        for v in vs:
            if v not in self.marked:
                self.toEdge[v] = s
                self.dfs(g, v)

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
dfs = DepthFirstSearch(g, 0)
print(dfs.pathTo(5))
print(dfs.pathTo(4))
