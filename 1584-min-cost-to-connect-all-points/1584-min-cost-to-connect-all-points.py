from functools import cmp_to_key


class Solution:

    def graph(self, n):
        self.n = n
        self.g = [[0 for i in range(n + 1)] for j in range(n + 1)]

    def manhat(self, x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])

    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.n):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.n
        parent = [None] * self.n  # Array to store constructed MST
        key[0] = 0
        mstSet = [False] * self.n

        parent[0] = -1  # First node is always the root of
        for cout in range(self.n):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.n):
                if self.g[u][v] > 0 and mstSet[
                        v] == False and key[v] > self.g[u][v]:
                    key[v] = self.g[u][v]
                    parent[v] = u
        return sum([self.g[i][parent[i]] for i in range(1, self.n)])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        self.graph(n)
        for i in range(n):
            for j in range(n):
                if i != j:
                    weight = self.manhat(points[i], points[j])
                    self.g[i][j] = weight
        return self.primMST()
