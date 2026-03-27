class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        return [r[k % len(r):] + r[:k % len(r)] for r in mat] == mat