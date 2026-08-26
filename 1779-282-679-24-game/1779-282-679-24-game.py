class Solution:

    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6

        def dfs(nums: List[float]) -> bool:
            n = len(nums)
            if n == 1:
                return abs(nums[0] - 24.0) < EPS

            for i in range(n):
                for j in range(n):
                    if i != j:
                        a, b = nums[i], nums[j]
                        candidates = [a + b, a - b, b - a, a * b]
                        if abs(b) > EPS:
                            candidates.append(a / b)
                        if abs(a) > EPS:
                            candidates.append(b / a)

                        for val in candidates:
                            if dfs(
                                [nums[k]
                                 for k in range(n) if k not in [i, j]] +
                                    [val]):
                                return True
            return False

        return dfs([float(x) for x in cards])
