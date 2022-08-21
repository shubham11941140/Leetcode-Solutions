class Solution:

    @staticmethod
    def sn(n):
        return (n * (n + 1)) // 2

    @staticmethod
    def numberOfArithmeticSlices(nums: List[int]) -> int:
        n = len(nums)
        b = [nums[i + 1] - nums[i] for i in range(n - 1)]
        li = 0
        ri = -1
        c = []
        b.append(10**10)
        for i in range(1, n - 1):
            if b[i] != b[i - 1]:
                li = i
            if b[i] != b[i + 1]:
                ri = i
            if ri >= li and ri > -1:
                c.append([li, ri])
        ans = 0
        for left, right in c:
            t = right - left
            ans += (t * (t + 1)) // 2
        return ans
