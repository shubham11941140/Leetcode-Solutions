class Solution:
    
    def cycle(self, adj, visited, node, rec):
        rec[node] = True
        for i in adj[node]:            
            if not visited[i]:
                visited[i] = True
                if self.cycle(adj, visited, i, rec):
                    return True
            else:
                if rec[i]:
                    return True                    
        rec[node] = False
        return False                        
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = [[] for i in range(numCourses)]
        for i in prerequisites:
            adj[i[1]].append(i[0])
            if i[1] == i[0]:
                return False
            
        visited = [False] * numCourses
        rec = [False] * numCourses
        for i in range(numCourses):
            if not visited[i]:
                visited[i] = True
                if self.cycle(adj, visited, i, rec):
                    return False
        return True
        
