class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Create a graph using adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node, parent):
            total = values[node]
            num_components = 0
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                child_sum, child_components = dfs(neighbor, node)
                if child_sum % k == 0:
                    num_components += child_components + 1
                else:
                    total += child_sum
                    num_components += child_components
            return total, num_components
        total_sum, components = dfs(0, -1)
        return components + (total_sum % k == 0)       