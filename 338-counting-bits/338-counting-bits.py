class Solution:

    @staticmethod
    def countBits(n: int) -> List[int]:
        return [bin(i).count("1") for i in range(n + 1)]
