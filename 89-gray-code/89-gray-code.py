class Solution:

    @staticmethod
    def grayCode(n: int) -> List[int]:
        return [(i ^ (i >> 1)) for i in range(2**n)]
