class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = sum([i for i in nums if i % 2 == 0])
        res = []
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                s -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                s += nums[idx]
            res.append(s)
        return res        