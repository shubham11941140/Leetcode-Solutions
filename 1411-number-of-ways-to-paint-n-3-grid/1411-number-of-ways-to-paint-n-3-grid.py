class Solution:

    def numOfWays(self, n: int) -> int:
        x, y = 6, 6
        for i in range(2, n + 1):
            new_x = (3 * x + 2 * y) % (10**9 + 7)
            new_y = (2 * x + 2 * y) % (10**9 + 7)
            x, y = new_x, new_y
        return (x + y) % (10**9 + 7)
