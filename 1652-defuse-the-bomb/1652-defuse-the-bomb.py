class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        return [0] * n if not k else [sum(code[(i + j) % n] for j in range(1, k + 1)) if k > 0 else sum(code[(i + j) % n] for j in range(k, 0)) for i in range(n)]