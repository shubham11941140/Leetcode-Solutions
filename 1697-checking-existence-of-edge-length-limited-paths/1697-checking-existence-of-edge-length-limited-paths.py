class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # sort edges by distance
        edgeList.sort(key=lambda x: x[2])
        # sort queries by limit and record original index
        queries = sorted(enumerate(queries), key=lambda x: x[1][2])
        # initialize union find
        uf = UnionFind(n)
        # initialize answer list
        ans = [False] * len(queries)
        # iterate through queries
        i = 0 # pointer for edgeList
        for j, (p, q, limit) in queries:
            # union nodes that have distance less than limit
            while i < len(edgeList) and edgeList[i][2] < limit:
                uf.union(edgeList[i][0], edgeList[i][1])
                i += 1
            # check if p and q are connected
            ans[j] = uf.find(p) == uf.find(q)
        return ans

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)        