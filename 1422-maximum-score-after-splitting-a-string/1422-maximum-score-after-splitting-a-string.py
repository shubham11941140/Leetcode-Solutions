class Solution:
    def maxScore(self, s: str) -> int:
        one_int = s.count("1")  # Count of '1's in the string
        max_score = 0  # Maximum score
        for char in s[:-1]:
            if char == "1":
                one_int -= 1  # Decrement count of '1's
            else:
                one_int += 1  # Increment count of '0's
            max_score = max(max_score, one_int)
        return max_score
