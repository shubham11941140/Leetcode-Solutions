class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = "".join([i for i in str(n) if i != "0"])
        return int(s) * sum([int(i) for i in s]) if s else 0        