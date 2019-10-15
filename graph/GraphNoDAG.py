class Graph():
    g = {}
    g[0] = [5,1,6]
    g[1] = []
    g[2] = [0,3]
    g[3] = [5]
    g[4] = []
    g[5] = [4]
    g[6] = [9,4]
    g[7] = [6]
    g[8] = [7]
    g[9] = [11,10,12]
    g[10] = []
    g[11] = [12]
    g[12]=[]


    def adj(self, v):
        return self.g[v]

    def all(self):
        return range(12)

