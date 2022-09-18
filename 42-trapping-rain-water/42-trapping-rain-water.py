class Solution:

    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = [height[0]] * n
        r = [height[-1]] * n
        for i in range(1, n):
            l[i] = max(l[i - 1], height[i])
            r[-i - 1] = max(r[-i], height[-i - 1])
        return sum(min(l[i], r[i]) - height[i] for i in range(n))
