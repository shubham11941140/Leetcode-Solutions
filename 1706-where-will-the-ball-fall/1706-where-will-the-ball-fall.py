class Solution:

    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        ans = []
        for i in range(m):
            x = i
            for j in range(n):
                if grid[j][x] == 1:
                    if x + 1 < m and grid[j][x + 1] == 1:
                        x += 1
                    else:
                        ans.append(-1)
                        break
                else:
                    if x >= 1 and grid[j][x - 1] == -1:
                        x -= 1
                    else:
                        ans.append(-1)
                        break
            else:
                ans.append(x)
        return ans
