class Solution:

    @staticmethod
    def countQuadruplets(nums: List[int]) -> int:
        c1 = 0
        n = len(nums)
        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    for d in range(c + 1, n):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            c1 += 1
        return c1
