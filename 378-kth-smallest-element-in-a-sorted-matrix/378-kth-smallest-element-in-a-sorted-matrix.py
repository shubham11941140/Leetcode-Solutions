class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        s = []
        for i in matrix:
            s += i
        return sorted(s)[k - 1]
        