class Solution:

    @staticmethod
    def plusOne(digits: List[int]) -> List[int]:
        p = int("".join([str(i) for i in digits]))
        return [int(i) for i in str(p + 1)]
