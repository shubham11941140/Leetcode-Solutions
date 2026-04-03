class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)

        # Store robots as [position, distance]
        x = sorted([[robots[i], distance[i]] for i in range(n)])

        # Sort robots and walls
        walls.sort()

        # Dummy robot
        x.append([10**9, 0])

        # Function to count walls in range [l, r]
        def query(l, r):
            return bisect_right(walls, r) - bisect_left(walls, l) if l <= r else 0

        # dp[i][0] = shoot LEFT
        # dp[i][1] = shoot RIGHT
        dp = [[0, 0] for _ in range(n)]

        # Base case
        dp[0][0] = query(x[0][0] - x[0][1], x[0][0])

        if n > 1:
            dp[0][1] = query(x[0][0], min(x[1][0] - 1, x[0][0] + x[0][1]))
        else:
            dp[0][1] = query(x[0][0], x[0][0] + x[0][1])

        # DP transitions
        for i in range(1, n):

            # Case 1: shoot RIGHT
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]) + \
                       query(x[i][0], min(x[i + 1][0] - 1, x[i][0] + x[i][1]))

            # Case 2: shoot LEFT (no overlap)
            dp[i][0] = dp[i - 1][0] + \
                        query(max(x[i][0] - x[i][1], x[i - 1][0] + 1),x[i][0])

            # Case 3: shoot LEFT with overlap handling
            leftStart = max(x[i][0] - x[i][1], x[i - 1][0] + 1)

            overlapEnd = min(x[i - 1][0] + x[i - 1][1], x[i][0] - 1)

            res = dp[i - 1][1] + \
                  query(leftStart, x[i][0]) - query(leftStart, overlapEnd)

            dp[i][0] = max(dp[i][0], res)

        return max(dp[n - 1][0], dp[n - 1][1])