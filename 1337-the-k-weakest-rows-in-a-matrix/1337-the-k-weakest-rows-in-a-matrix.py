class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = [(mat[i].count(1), i) for i in range(len(mat))]
        r = [y for x, y in sorted(ans)]
        print(r[:k])
        return r[:k]
        