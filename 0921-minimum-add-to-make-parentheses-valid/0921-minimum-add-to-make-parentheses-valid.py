class Solution:

    def minAddToMakeValid(self, s: str) -> int:
        additions_needed = unmatched_open = 0
        for char in s:
            if char == "(":
                unmatched_open += 1
            else:
                if unmatched_open > 0:
                    unmatched_open -= 1
                else:
                    additions_needed += 1
        return additions_needed + unmatched_open
