class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums[:]

        # Build prefix max left→right
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])

        # Build suffix min right→left
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        # Single sweep: assign component max to each element
        ans = [0] * n
        start = 0
        for i in range(n - 1):
            if prefix_max[i] <= suffix_min[i + 1]:   # clean boundary here
                for k in range(start, i + 1):
                    ans[k] = prefix_max[i]            # = max of this component
                start = i + 1
        for k in range(start, n):                     # last component
            ans[k] = prefix_max[n - 1]
        return ans