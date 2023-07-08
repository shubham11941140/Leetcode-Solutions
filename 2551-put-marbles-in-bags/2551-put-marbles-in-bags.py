class Solution:

    def putMarbles(self, weights: List[int], k: int) -> int:
        length = len(weights)
        if k in [1, length]:
            return 0
        answer = 0
        ans1 = 0
        k -= 1
        res1 = [(weights[i] + weights[i + 1]) for i in range(length - 1)]
        result = sorted(res1)
        res1.sort(reverse=True)
        for i in range(k):
            ans1 += res1[i]
        for i in range(k):
            answer += result[i]
        return ans1 - answer
