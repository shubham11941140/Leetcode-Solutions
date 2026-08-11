class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        i = j = k
        min_num = nums[k]
        res = min_num
        n = len(nums)

        while i > 0 or j < n - 1:
            if (nums[i - 1] if i else 0) < (nums[j + 1] if j < n - 1 else 0):
                j += 1
            else:
                i -= 1
            min_num = min(min_num, nums[i], nums[j])
            res = max(res, min_num * (j - i + 1))

        return res
