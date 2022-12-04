class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        s = [0] * (n + 1)
        for i in range(n):
            s[i + 1] = s[i] + nums[i]
        ans = 10 ** 9
        idx = -1
        for i in range(n):
            a = (s[i + 1] - s[0]) // (i + 1)
            b = (s[n] - s[i + 1]) // (n - i - 1) if n - i - 1 else 0
            d = abs(a - b)
            if d < ans:
                ans = d
                idx = i
        return idx