class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = sorted([(nums[i], i) for i in range(n)])
        l = 0
        r = n - 1
        while l < r:
            s = d[l][0] + d[r][0]
            if s == target:
                return [d[l][1], d[r][1]]
            elif s < target:
                l += 1
            else:
                r -= 1
