class Solution:

    def minimizeArrayValue(self, nums: List[int]) -> int:
        mn = 0
        nums = list(accumulate(nums))
        for i, n in enumerate(nums):
            mn = max(mn, ceil(n / (i + 1)))
        return mn

        n = len(nums)
        lval = min(nums)
        for i in range(n):
            nums[i] = nums[i] - lval
        for _ in range(1000):
            c = nums.copy()
            for i in range(1, n):  # (n - 1, 0, -1):
                if nums[i - 1] < nums[i]:
                    s = nums[i - 1] + nums[i]
                    if s % 2 == 0:
                        nums[i - 1] = s // 2
                        nums[i] = s // 2
                    else:
                        nums[i - 1] = s // 2 + 1
                        nums[i] = s // 2
            # Check if the first number is maximum
            if nums[0] == max(nums) and nums.count(max(nums)) == 1:
                # print(1515151515, _)
                # print(nums)
                break
            if c == nums:
                # print(_)
                break
        return max(nums) + lval
