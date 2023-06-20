class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        res = [-1] * n
        #print(prefix_sum)
        for i in range(n):
            if i >= k and i + k + 1 < n + 1:
                #print(i)
                r = prefix_sum[i + k + 1]
                l = prefix_sum[i - k]   
                avg = (r - l)//(2 *k + 1)
                #print(i, r, l, (r - l)//(2 *k + 1))
                res[i] = avg
        return res