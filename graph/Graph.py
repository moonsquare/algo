class Graph():
    g = {}
    g[0] = [5,1]
    g[1] = []
    g[2] = [0,3]
    g[3] = [5,2]
    g[4] = [3,2]
    g[5] = [4]
    g[6] = [9,4,0]
    g[7] = [6,8]
    g[8] = [7,9]
    g[9] = [11,10]
    g[10] = [12]
    g[11] = [4,12]
    g[12]=[9]


    def adj(self, v):
        return self.g[v]

    def all(self):
        return range(12)

