class Solution:
    
    
    def dfs(self, v, graph, visited, node):
        for i in graph[node]:                 
            if visited[i] == -1:
                if visited[node] == 0:
                    visited[i] = 1
                elif visited[node] == 1:
                    visited[i] = 0

                if not self.dfs(v, graph, visited, i):
                    return False
            elif visited[i] != -1 and visited[node] == visited[i]:
                return False
        return True          
        
    def isBipartite(self, graph: List[List[int]]) -> bool:

        v = len(graph)
        visited = [-1] * v
        
        for i in range(v):
            if visited[i] == -1:
                visited[i] = 1
                f = self.dfs(v, graph, visited, i)                
                if f == False:
                    return False       
        return True
            
            
        