class Solution:

    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # Count of distinct elements in the array
        total_distinct = len(set(nums))
        count = Counter()
        left = 0
        result = 0

        for right in range(len(nums)):
            count[nums[right]] += 1

            # Shrink the window until it contains all distinct elements
            while len(count) == total_distinct:
                # Count subarrays ending at 'right'
                result += len(nums) - right
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1

        return result
