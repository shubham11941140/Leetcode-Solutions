class Solution:

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return any(a == b and a != 0 for a, b in zip(nums, nums[1:]))
        if k < 0:
            k = -k
        prefix = 0
        seen = {0: -1}
        for i, n in enumerate(nums):
            prefix = (prefix + n) % k
            if prefix in seen:
                if i - seen[prefix] > 1:
                    return True
            else:
                seen[prefix] = i
        return False
