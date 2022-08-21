class Solution:

    def bridges(self, u):

        self.visited[u] = True
        self.disc[u] = self.time
        self.low[u] = self.time
        self.time += 1

        for v in self.adj[u]:

            if not self.visited[v]:

                self.parent[v] = u

                self.bridges(v)

                self.low[u] = min(self.low[u], self.low[v])

                if self.low[v] > self.disc[u]:
                    self.ans.append([u, v])

            elif v != self.parent[u]:
                self.low[u] = min(self.low[u], self.disc[v])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        self.ans = []
        self.time = 0
        self.adj = [[] for _ in range(n)]

        for i, j in connections:

            self.adj[i].append(j)
            self.adj[j].append(i)

        self.visited = [False for _ in range(n)]
        self.disc = [10 ** 10 for _ in range(n)]
        self.low = [10 ** 10 for _ in range(n)]
        self.parent = [-1 for _ in range(n)]

        for i in range(n):
            if not self.visited[i]:
                self.bridges(i)
        return self.ans
