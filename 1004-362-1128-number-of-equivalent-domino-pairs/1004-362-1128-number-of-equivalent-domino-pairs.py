class Solution:

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        return sum(
            [
                (i * (i - 1)) // 2
                for i in Counter([tuple(sorted(j)) for j in dominoes]).values()
            ]
        )
