class Solution:

    @staticmethod
    def sortByBits(arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count("1"), x))
