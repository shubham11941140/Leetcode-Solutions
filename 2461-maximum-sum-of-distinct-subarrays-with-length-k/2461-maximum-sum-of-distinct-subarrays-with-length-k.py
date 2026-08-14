class Solution:

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return 0
        max_sum = 0
        window_sum = 0
        ec = {}
        for i in range(len(nums)):
            ec[nums[i]] = ec[nums[i]] + 1 if nums[i] in ec else 1
            window_sum += nums[i]
            if i >= k:
                left_elem = nums[i - k]
                window_sum -= left_elem
                if ec[left_elem] == 1:
                    del ec[left_elem]
                else:
                    ec[left_elem] -= 1
            if len(ec) == k:
                max_sum = max(max_sum, window_sum)
        return max_sum
