class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [y for x, y in sorted([(mat[i].count(1), i) for i in range(len(mat))])][:k]
        
