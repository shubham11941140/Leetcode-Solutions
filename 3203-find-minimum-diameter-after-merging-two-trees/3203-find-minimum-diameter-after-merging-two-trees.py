class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def bfs(u, graph): 
            ans = 0 
            queue = deque([(u, -1)])
            while queue:
                ans += 1
                for _ in range(len(queue)): 
                    u, p = queue.popleft()
                    for v in graph[u]: 
                        if v != p: 
                            queue.append((v, u))
            return ans, u        
        def fn(edges): 
            n = len(edges)+1
            graph = [[] for _ in range(n)]
            for u, v in edges: 
                graph[u].append(v)
                graph[v].append(u)
            _, u = bfs(0, graph)
            dia, _ = bfs(u, graph)
            return dia        
        cnt1 = fn(edges1)
        cnt2 = fn(edges2)
        return max(cnt1 - 1, cnt2 - 1, cnt1 // 2 + cnt2 // 2 + 1)