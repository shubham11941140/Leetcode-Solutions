class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = sum([i for i in nums if not (i % 2)])
        res = []
        for val, idx in queries:
            if not (nums[idx] % 2):
                s -= nums[idx]
            nums[idx] += val
            if not (nums[idx] % 2):
                s += nums[idx]
            res.append(s)
        return res      