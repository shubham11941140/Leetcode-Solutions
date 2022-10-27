class Solution:   
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        a = [(i, j) for i in range(n) for j in range(n) if img1[i][j]]
        b = [(i, j) for i in range(n) for j in range(n) if img2[i][j]]
        d = Counter([(bx - ax, by - ay) for ax, ay in a for bx, by in b])
        return max(d.values() or [0])