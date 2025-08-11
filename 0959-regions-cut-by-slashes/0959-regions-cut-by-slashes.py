class Solution:

    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = list(range(4 * n * n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for i in range(n):
            for j in range(n):
                root = 4 * (i * n + j)
                if grid[i][j] == "/":
                    union(root + 0, root + 3)
                    union(root + 1, root + 2)
                elif grid[i][j] == "\\":
                    union(root + 0, root + 1)
                    union(root + 2, root + 3)
                else:
                    union(root + 0, root + 1)
                    union(root + 1, root + 2)
                    union(root + 2, root + 3)

                if i > 0:
                    union(root + 0, root - 4 * n + 2)
                if j > 0:
                    union(root + 3, root - 4 + 1)

        return sum(parent[x] == x for x in range(4 * n * n))
