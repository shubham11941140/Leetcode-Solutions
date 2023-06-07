class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        for i in range(32):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            bit_c = (c >> i) & 1
            if bit_c == 0:
                res += bit_a + bit_b
            else:
                if bit_a + bit_b == 0:
                    res += 1
        return res        