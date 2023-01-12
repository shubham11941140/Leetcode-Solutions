class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        ans = [0] * n
        def dfs(node, parent):
            count = collections.Counter()
            for nei in graph[node]:
                if nei != parent:
                    count += dfs(nei, node)
            count[labels[node]] += 1
            ans[node] = count[labels[node]]
            return count
        dfs(0, None)
        return ans        