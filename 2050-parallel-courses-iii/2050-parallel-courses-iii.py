class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        maxTime = time.copy()

        for edge in relations:
            graph[edge[0] - 1].append(edge[1] - 1)
            indegree[edge[1] - 1] += 1

        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                maxTime[neighbor] = max(maxTime[neighbor], maxTime[node] + time[neighbor])
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return max(maxTime)

        