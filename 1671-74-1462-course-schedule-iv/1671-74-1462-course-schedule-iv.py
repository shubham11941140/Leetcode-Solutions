class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        a = [[False] * numCourses for _ in range(numCourses)]        
        # Set direct prerequisites to True in the matrix
        for u, v in prerequisites:
            a[u][v] = True        
        # Floyd-Warshall algorithm to compute the transitive closure
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    a[i][j] = a[i][j] or (a[i][k] and a[k][j])        
        # Answer the queries based on the adjacency matrix
        return [a[u][v] for u, v in queries]  