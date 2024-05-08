class Solution:

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort = sorted(score)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(
            map(str, range(4, len(score) + 1))
        )
        return list(map(dict(zip(sort, rank)).get, score))
