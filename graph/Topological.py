import DirectedCycle as dc
import DepthFirstOrder as dfo
import GraphNoDAG
import Graph

class Topological:
    def __init__(self,G):
        self.__directedCycle=dc.DirectedCycle(G)
        if (self.__directedCycle.hasCycle()==False):
            self.__depthFirstOrder=dfo.DepthFirstOrder(G)
            self.__order=self.__depthFirstOrder.rePost()
    def order(self):
        return self.__order


g=GraphNoDAG.Graph()
t=Topological(g)
o=t.order()
while not o.empty():
    print(o.get())
