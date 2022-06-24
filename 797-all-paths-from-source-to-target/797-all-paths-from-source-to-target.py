class Solution:
    
    def dfs(self, graph, a, u, k):
        for i in graph[u]:
            a[k].append(u)
            a[k].append(i)
            self.dfs(graph, a, i, k)
            k += 1
    
    def pdfs(self, graph, node, curr, final):
        if node == final:
            return
        a = curr[-1].copy()
        for i in graph[node]:
            curr.append(a + [i])
            self.pdfs(graph, i, curr, final)
        
                                
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        curr = [[0]]
        node = 0
        final = n - 1
        self.pdfs(graph, node, curr, final)
        print(curr)
        return [i for i in curr if i[0] == node and i[-1] == final]
        
        
                