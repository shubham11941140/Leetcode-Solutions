class Solution:

    def minFlipsMonoIncr(self, s: str) -> int:
        flips = 0
        ones = 0
        for c in s:
            if c == "0":
                if ones:
                    flips += 1
            else:
                ones += 1
            if flips > ones:
                flips = ones
        return flips
