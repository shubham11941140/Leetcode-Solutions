class Solution:

    def minimumAverageDifference(self, nums: List[int]) -> int:
        # Find prefix sum
        n = len(nums)
        s = [0] * (n + 1)
        for i in range(n):
            s[i + 1] = s[i] + nums[i]
        # Find average difference of each index
        ans = 10**9
        idx = -1
        for i in range(n):
            # Sum of first half
            l = s[i + 1] - s[0]
            # Sum of second half
            r = s[n] - s[i + 1]
            # average of first half
            a = l // (i + 1)
            # average of second half
            if n - i - 1 > 0:
                b = r // (n - i - 1)
            else:
                b = 0
            # average difference
            d = abs(a - b)
            if d < ans:
                ans = d
                idx = i
        # Return the index
        return idx
