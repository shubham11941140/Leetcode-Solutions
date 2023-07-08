class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        length = len(weights)
        if k in [1, length]:
            return 0
        answer = 0
        ans1 = 0
        res1 = sorted([(weights[i] + weights[i + 1]) for i in range(length - 1)], reverse = True)
        result = res1[::-1]
        return sum([(res1[i] - result[i]) for i in range(k - 1)])
      