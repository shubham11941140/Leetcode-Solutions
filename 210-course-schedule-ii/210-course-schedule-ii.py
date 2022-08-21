class Solution:

    def topological_sort(self, adj, visited, node, stack):
        for i in adj[node]:
            if not visited[i]:
                visited[i] = True
                self.topological_sort(adj, visited, i, stack)
        stack.append(node)

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

    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        for i in prerequisites:
            adj[i[1]].append(i[0])
            if i[1] == i[0]:
                return []

        visited = [False] * numCourses
        rec = [False] * numCourses
        for i in range(numCourses):
            if not visited[i]:
                visited[i] = True
                if self.cycle(adj, visited, i, rec):
                    return []

        visited = [False] * numCourses
        ans = []
        for i in range(numCourses):
            if not visited[i]:
                visited[i] = True
                stack = []
                self.topological_sort(adj, visited, i, stack)
                ans += stack
        return ans[::-1]
