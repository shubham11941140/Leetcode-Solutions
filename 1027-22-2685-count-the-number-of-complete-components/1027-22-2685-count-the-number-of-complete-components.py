class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Helper function to perform DFS and gather component nodes
        def dfs(node, component):
            visited.add(node)
            component.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)        
        # Create the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)        
        visited = set()
        complete_count = 0        
        # Traverse each node
        for node in range(n):
            if node not in visited:
                component = set()
                dfs(node, component)                
                # Check if the component is complete
                is_complete = True
                for u in component:
                    if len(graph[u]) != len(component) - 1:
                        is_complete = False
                        break
                if is_complete:
                    complete_count += 1        
        return complete_count      