class Solution:

    @staticmethod
    def superPow(a: int, b: List[int]) -> int:
        return pow(a, int("".join([str(i) for i in b])), 1337)
