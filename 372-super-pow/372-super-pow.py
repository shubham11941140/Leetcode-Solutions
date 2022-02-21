class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        b = int(''.join([str(i) for i in b]))
        return pow(a, b, 1337)
        