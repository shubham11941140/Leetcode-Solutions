class Solution:

    def numRabbits(self, answers: List[int]) -> int:
        d = defaultdict(int)
        for i in answers:
            d[i] += 1
        ans = 0
        for i, j in d.items():
            ans += (j + i) // (i + 1) * (i + 1)
        return ans
