from collections import Counter

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:       
        if not poured:
            return 0
        c = [[0 for i in range(101)] for j in range(101)]
        c[0][0] = poured
        for r in range(query_row + 1):
            for col in range(r + 1):
                left = (c[r][col] - 1) / 2
                if left > 0:
                    c[r + 1][col] += left
                    c[r + 1][col + 1] += left
        return min(1, c[query_row][query_glass])