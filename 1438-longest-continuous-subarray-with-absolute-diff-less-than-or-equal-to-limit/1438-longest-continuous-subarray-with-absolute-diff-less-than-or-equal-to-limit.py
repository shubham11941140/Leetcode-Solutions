class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque, min_deque = deque(), deque()
        left = 0
        max_length = 0

        for right, num in enumerate(nums):
            # Maintain a decreasing monotonic queue for maximum values
            while max_deque and nums[max_deque[-1]] < num:
                max_deque.pop()
            max_deque.append(right)

            # Maintain an increasing monotonic queue for minimum values
            while min_deque and nums[min_deque[-1]] > num:
                min_deque.pop()
            min_deque.append(right)
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                if max_deque[0] == left:
                    max_deque.popleft()
                if min_deque[0] == left:
                    min_deque.popleft()
                left += 1

            # Update the maximum subarray length
            max_length = max(max_length, right - left + 1)

        return max_length
