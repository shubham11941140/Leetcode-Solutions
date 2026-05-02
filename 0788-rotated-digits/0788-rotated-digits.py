class Solution:
    def rotatedDigits(self, n: int) -> int:
        return sum((q := {*str(v + 1)}) <= {*'0182569'} and not q <= {*'018'} for v in range(n))