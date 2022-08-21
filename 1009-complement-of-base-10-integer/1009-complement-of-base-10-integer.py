class Solution:

    @staticmethod
    def bitwiseComplement(n: int) -> int:
        return 2**len(bin(n)[2:]) - 1 - n
