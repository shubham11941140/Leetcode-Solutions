class Solution:

    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        # Initialize max_i to A[0] + 0 since we're at index 0
        max_i = values[0]
        for j in range(1, len(values)):
            max_score = max(max_score, max_i + values[j] - j)
            max_i = max(max_i, values[j] + j)
        return max_score
