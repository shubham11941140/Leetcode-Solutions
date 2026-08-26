class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c = s.count("1")
        return "" if not c else "1" * (c - 1) + (len(s) - c) * "0" + "1"
