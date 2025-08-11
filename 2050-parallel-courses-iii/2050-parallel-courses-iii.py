class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        m = time.copy()

        for edge in relations:
            graph[edge[0] - 1].append(edge[1] - 1)
            indegree[edge[1] - 1] += 1

        queue = deque([i for i in range(n) if not indegree[i]])
        while queue:
            node = queue.popleft()

            for i in graph[node]:
                m[i] = max(m[i], m[node] + time[i])
                indegree[i] -= 1
                if not indegree[i]:
                    queue.append(i)
        return max(m)
