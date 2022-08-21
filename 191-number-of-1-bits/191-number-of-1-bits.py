class Solution:

    @staticmethod
    def hammingWeight(n: int) -> int:
        return bin(n).count("1")
