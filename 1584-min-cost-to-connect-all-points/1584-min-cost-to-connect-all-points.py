from functools import cmp_to_key

class Solution:
        
    def graph(self, n):
        self.n = n
        self.g = [[0 for i in range(n + 1)] for j in range(n + 1)]
        
    def manhat(self, x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])
    
    def print(self, parent):
        ans = 0
        #print ("Edge \tWeight")
        for i in range(1, self.n):
            ans += self.g[i][parent[i]]
            #print (parent[i], "-", i, "\t", self.g[i][parent[i]])
        return ans
    
    def minKey(self, key, mstSet):
 
        min = sys.maxsize
 
        for v in range(self.n):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
 
        return min_index

    def primMST(self):
 
        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.n
        parent = [None] * self.n # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.n
 
        parent[0] = -1 # First node is always the root of
 
        for cout in range(self.n):

            u = self.minKey(key, mstSet)

            mstSet[u] = True
 
            for v in range(self.n):
 
                if self.g[u][v] > 0 and mstSet[v] == False and key[v] > self.g[u][v]:
                        key[v] = self.g[u][v]
                        parent[v] = u
 
        return self.print(parent)
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        
        # Make a complete graph with edges between all points with weight as manhattan
        # MST Weight is the answer
        n = len(points)
        self.graph(n)
        for i in range(n):
            for j in range(n):
                if i != j:
                    weight = self.manhat(points[i], points[j])
                    self.g[i][j] = weight                    
        #print(self.g)
        ans = self.primMST()
        return ans
        
        
        
        
        
        # Sorted based on the key
        ans = 0
        n = len(points)
        
        for i in range(n):
            m = min([self.manhat(points[i], points[j]) for j in range(n) if i != j])
            ans += m
        print(ans)
                    
        
        
        
        
        p = sorted([sum(i) for i in points])
        print(p)
        
        points.sort(key=cmp_to_key(self.compare))
        print(points)
        ans = 0
        for i in range(len(points) - 1):
            ans += self.compare(points[i], points[i + 1])
        return ans
        
        