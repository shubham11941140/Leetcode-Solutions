from collections import Counter


class Solution:

    def reorderedPowerOf2(self, n: int) -> bool:
        return any(
            Counter(list(str(n))) == Counter(list(str(2**i)))
            for i in range(30))
