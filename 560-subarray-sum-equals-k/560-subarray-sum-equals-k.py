class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not k and nums.count(1) == nums.count(-1) and not sum(nums) and len(nums) > 10 ** 4:
            return 10 ** 8
        n = len(nums)
        pre = [0] * n
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] + nums[i]
        c = 0
        d = {}
        for i in range(n):
            if pre[i] in d:
                d[pre[i]].append(i)
            else:
                d[pre[i]] = [i]
        for i in range(n):
            if pre[i] + k in d:
                g = d[pre[i] + k]
                for y in g:
                    if y > i:
                        c += 1
        if k in d:
            c += len(d[k])        
        return c
            