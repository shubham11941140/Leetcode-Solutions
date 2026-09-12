class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        return max(
            0,
            max(
                [
                    sum([satisfaction[j] * (j - i + 1) for j in range(i, n)])
                    for i in range(n)
                ]
            ),
        )
