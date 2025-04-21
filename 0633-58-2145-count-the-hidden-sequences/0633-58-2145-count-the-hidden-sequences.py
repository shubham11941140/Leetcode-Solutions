class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_val, max_val, current = 0, 0, 0
        for diff in differences:
            current += diff
            min_val = min(min_val, current)
            max_val = max(max_val, current)
        return max(0, (upper - lower + 1) - (max_val - min_val))     