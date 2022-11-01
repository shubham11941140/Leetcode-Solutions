class Solution:

    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        for i, j in Counter(answers).items():
            ans += (j + i) // (i + 1) * (i + 1)
        return ans
