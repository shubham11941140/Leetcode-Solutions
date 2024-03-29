class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        l = len(weights)
        if k in [1, l]:
            return 0
        res1 = sorted([(weights[i] + weights[i + 1]) for i in range(l - 1)], reverse = True)
        result = res1[::-1]
        return sum([(res1[i] - result[i]) for i in range(k - 1)])
      