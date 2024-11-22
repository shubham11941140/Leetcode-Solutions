class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_count = defaultdict(int)
        for row in matrix:
            pattern_count["".join("1" if x == row[0] else "0" for x in row)] += 1
        return max(pattern_count.values())
