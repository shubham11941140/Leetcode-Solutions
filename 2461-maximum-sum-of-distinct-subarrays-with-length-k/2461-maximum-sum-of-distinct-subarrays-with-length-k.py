class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return 0

        max_sum = 0
        window_sum = 0
        element_count = {}

        for i in range(len(nums)):
            # Add the current element to the window
            if nums[i] in element_count:
                element_count[nums[i]] += 1
            else:
                element_count[nums[i]] = 1
            window_sum += nums[i]
            if i >= k:
                left_elem = nums[i - k]
                window_sum -= left_elem
                if element_count[left_elem] == 1:
                    del element_count[left_elem]
                else:
                    element_count[left_elem] -= 1
            if len(element_count) == k:
                max_sum = max(max_sum, window_sum)
        return max_sum        