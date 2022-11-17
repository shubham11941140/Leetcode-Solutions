class Solution:
    def computeArea(
        self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int
    ) -> int:
        return (
            (C - A) * (D - B) + (G - E) * (H - F)
            if E >= C or G <= A or F >= D or H <= B
            else (C - A) * (D - B)
            + (G - E) * (H - F)
            - (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
        )
