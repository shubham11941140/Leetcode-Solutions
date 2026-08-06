class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        i = n
        while True:
            v = 1
            for j in str(i):
                v *= int(j)
            if v % t == 0:
                return i
            i += 1