class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        l = [0] + sorted(horizontalCuts) + [h]
        b = [0] + sorted(verticalCuts) + [w]
        ml = max([(l[i + 1] - l[i]) for i in range(len(l) - 1)])
        mb = max([(b[i + 1] - b[i]) for i in range(len(b) - 1)])
        return (ml * mb) % (10 ** 9 + 7)
        