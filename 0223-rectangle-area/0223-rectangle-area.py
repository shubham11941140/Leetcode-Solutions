class Solution:
    def computeArea(
        self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int
    ) -> int:
        if E >= C or G <= A or F >= D or H <= B:
            return (C - A) * (D - B) + (G - E) * (H - F)
        return (
            (C - A) * (D - B)
            + (G - E) * (H - F)
            - (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
        )
