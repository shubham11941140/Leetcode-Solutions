class Solution:
   
    def dfs(self, node):
        if node == self.n - 1:
            return
        a = self.curr[-1].copy()
        for i in self.graph[node]:
            self.curr.append(a + [i])
            self.dfs(i)        
                                
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.n = len(graph)
        self.curr = [[0]]
        self.dfs(0)
        return [i for i in self.curr if i[-1] == self.n - 1]
        
        
                