class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        need = total % p
        if need == 0:
            return 0
        mp = {0: -1}
        prefix = 0
        res = len(nums)
        for i, x in enumerate(nums):
            prefix = (prefix + x) % p
            target = (prefix - need) % p
            if target in mp:
                res = min(res, i - mp[target])
            mp[prefix] = i
        return res if res < len(nums) else -1        