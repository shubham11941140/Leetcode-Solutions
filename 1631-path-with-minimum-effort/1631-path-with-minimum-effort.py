class Solution:

    def valid(self, i, j, n, m):
        return 0 <= i < n and 0 <= j < m

    def bfs(self, a, n, m, effort):
        v = [[False for j in range(m)] for i in range(n)]
        q = [(0, 0)]
        while q:
            i, j = q.pop(0)
            if i == n - 1 and j == m - 1:
                return True
            move = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for x, y in move:
                if self.valid(x, y, n, m):
                    if not v[x][y]:
                        if abs(a[i][j] - a[x][y]) <= effort:
                            v[x][y] = True
                            q.append((x, y))
        return False

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        left = 0
        right = max([max(i) for i in heights]) + 100
        while left < right:
            mid = (left + right) // 2
            if right - left <= 20:
                for i in range(left, right + 1):
                    if self.bfs(heights, n, m, i):
                        return i
            if self.bfs(heights, n, m, mid):
                right = mid
            else:
                left = mid + 1
