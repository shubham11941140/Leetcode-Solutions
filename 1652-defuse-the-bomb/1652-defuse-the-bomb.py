class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n

        if k == 0:
            return result

        for i in range(n):
            if k > 0:
                result[i] = sum(code[(i + j) % n] for j in range(1, k + 1))
            else:
                result[i] = sum(code[(i + j) % n] for j in range(k, 0))

        return result
        