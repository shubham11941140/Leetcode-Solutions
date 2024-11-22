class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        from collections import defaultdict

        def rowToPattern(row):
            # Create a pattern string where flipping columns will result in the same row
            first_val = row[0]
            return ''.join('1' if x == first_val else '0' for x in row)

        pattern_count = defaultdict(int)

        for row in matrix:
            pattern = rowToPattern(row)
            pattern_count[pattern] += 1

        return max(pattern_count.values())
        