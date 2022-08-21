class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = []
        s = set()
        for i in range(n):
            node = (1 << i, i, 0)
            q.append(node)
            s.add(node)
        while q:
            mask, curr, cost = q.pop(0)
            if mask == (1 << n) - 1:
                return cost
            for v in graph[curr]:
                newnode = (mask | (1 << v)), v, cost + 1
                if newnode not in s:
                    q.append(newnode)
                    s.add(newnode)        
        
