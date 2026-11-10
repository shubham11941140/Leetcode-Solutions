class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        a = b = c = 0
        for x in costs:
            a, b, c = b + 5, c + 3, x + min(a, b, c) + 1
        return c