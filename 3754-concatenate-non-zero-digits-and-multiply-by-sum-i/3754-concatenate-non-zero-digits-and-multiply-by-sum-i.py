class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if not n:
            return n
        s = "".join([i for i in str(n) if i != "0"])
        s1 = [int(i) for i in s]
        print(s, s1)
        return int(s) * sum(s1)
        