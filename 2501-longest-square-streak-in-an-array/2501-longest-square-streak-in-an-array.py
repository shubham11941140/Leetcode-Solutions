class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # Sort and convert list to a set for quick lookup
        nums.sort()
        num_set = set(nums)        
        longest_streak = 0
        for num in nums:
            streak_length = 0
            current = num
            while current in num_set:
                streak_length += 1
                current *= current  # Square the current number
            if streak_length >= 2:
                longest_streak = max(longest_streak, streak_length)
        return longest_streak if longest_streak >= 2 else -1       