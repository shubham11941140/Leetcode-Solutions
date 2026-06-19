class Solution:

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        return list(
            map(
                dict(
                    zip(
                        sorted(score)[::-1],
                        ["Gold Medal", "Silver Medal", "Bronze Medal"]
                        + list(map(str, range(4, len(score) + 1))),
                    )
                ).get,
                score,
            )
        )
