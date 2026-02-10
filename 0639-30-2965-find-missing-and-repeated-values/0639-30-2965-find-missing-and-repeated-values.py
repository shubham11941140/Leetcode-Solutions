class Solution:

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        b = []
        for i in grid:
            b += i
        c = [i for i in range(1, len(grid) ** 2 + 1) if b.count(i) in [0, 2]]
        return c[::-1] if c[0] not in b else c
