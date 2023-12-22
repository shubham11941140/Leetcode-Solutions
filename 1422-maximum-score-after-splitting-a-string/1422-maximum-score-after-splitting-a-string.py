class Solution:
    def maxScore(self, s: str) -> int:
        one_int = s.count('1')  # Count of '1's in the string
        zero_int = 0  # Count of '0's in the left substring
        max_score = 0  # Maximum score
        for char in s[:-1]:
            if char == '1':
                one_int -= 1  # Decrement count of '1's
            else:
                zero_int += 1  # Increment count of '0's
            current_score = zero_int + one_int
            max_score = max(max_score, current_score)
        return max_score        