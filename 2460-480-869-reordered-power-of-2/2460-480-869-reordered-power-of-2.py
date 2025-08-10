class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return True in [Counter(str(n)) == Counter(str(2 ** i)) for i in range(30)]