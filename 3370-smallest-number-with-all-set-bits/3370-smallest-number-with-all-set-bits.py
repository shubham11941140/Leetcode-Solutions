class Solution:

    def smallestNumber(self, n: int) -> int:
        for i in range(1, 11):
            if 2**i - 1 >= n:
                return 2**i - 1
