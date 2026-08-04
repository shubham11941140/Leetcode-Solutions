class Solution:

    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        max_odd = 0
        min_even = float("inf")

        for count in freq.values():
            if count % 2 == 1:  # Odd frequency
                max_odd = max(max_odd, count)
            else:  # Even frequency
                min_even = min(min_even, count)

        return max_odd - min_even if min_even != float("inf") else 0
