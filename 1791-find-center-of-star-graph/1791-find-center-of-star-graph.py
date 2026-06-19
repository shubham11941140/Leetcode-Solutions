class Solution:

    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 10
        adj = [[] for i in range(n)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        # print(adj)
        l = [len(i) for i in adj]
        # print(l)
        return l.index(max(l))
