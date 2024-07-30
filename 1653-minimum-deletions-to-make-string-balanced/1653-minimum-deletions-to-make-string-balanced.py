class Solution:
    def minimumDeletions(self, s: str) -> int:
        b = 0
        m = 0
        for char in s:
            if char == 'a':
                m = min(m + 1, b)
            else:
                b += 1   
        return m        