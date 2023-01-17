class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flips = 0
        ones = 0
        for i in range(len(s)):
            if s[i] == '0':
                if ones > 0:
                    flips += 1
            else:
                ones += 1
            if flips > ones:
                flips = ones
        return flips        