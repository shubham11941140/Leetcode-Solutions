class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        for u, v in pairs:
            graph[u].append(v)
            out_degree[u] += 1
            in_degree[v] += 1
        # Find the starting node for Eulerian path
        start = pairs[0][0]
        for node in out_degree:
            if out_degree[node] - in_degree[node] == 1:
                start = node
                break
        # Hierholzer's algorithm to find Eulerian path
        def findEulerianPath(start):
            stack = [start]
            path = []
            while stack:
                node = stack[-1]
                if graph[node]:
                    next_node = graph[node].pop()
                    stack.append(next_node)
                else:
                    path.append(stack.pop())
            return path[::-1]
        e = findEulerianPath(start)
        return [[e[i], e[i + 1]] for i in range(len(e) - 1)]       