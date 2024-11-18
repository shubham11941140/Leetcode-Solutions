class Solution:

    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n

        if k == 0:
            return result
        return [
            (
                sum(code[(i + j) % n] for j in range(1, k + 1))
                if k > 0
                else sum(code[(i + j) % n] for j in range(k, 0))
            )
            for i in range(n)
        ]
