class Solution:

    def putMarbles(self, weights: List[int], k: int) -> int:
        length = len(weights)
        if k == 1 or k == length:
            return 0
        answer = 0
        ans1 = 0
        k -= 1
        res1 = []
        for i in range(length - 1):
            res1.append(weights[i] + weights[i + 1])
        result = res1.copy()
        res1.sort(reverse=True)
        result.sort()
        for i in range(k):
            ans1 += res1[i]
        for i in range(k):
            answer += result[i]
        return ans1 - answer
