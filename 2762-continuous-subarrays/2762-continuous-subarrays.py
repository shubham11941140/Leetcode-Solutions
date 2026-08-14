from sortedcontainers import SortedList


class Solution:

    def continuousSubarrays(self, nums: List[int]) -> int:
        sl = SortedList([])
        nums.append(-5)
        start = 0
        sl.add(nums[start])
        count = 0
        for i in range(1, len(nums)):
            added = nums[i]
            sl.add(added)
            while abs(added - sl[0]) > 2 or abs(added - sl[-1]) > 2:
                subArrays = len(sl) - 1
                count += subArrays
                # Remove the leftmost element from the window
                sl.remove(nums[start])
                # Move the sliding window start position
                start += 1
        return count
