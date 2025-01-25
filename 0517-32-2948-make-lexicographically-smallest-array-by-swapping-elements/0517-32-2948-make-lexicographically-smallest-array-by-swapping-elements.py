class Solution:

    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # Create a sorted copy of nums to determine levels
        sorted_nums = sorted(nums)
        # Map of levels to their elements (sorted in deque)
        levels = defaultdict(deque)
        level_map = {}  # Element to level mapping
        current_level = 0
        levels[current_level].append(sorted_nums[0])
        level_map[sorted_nums[0]] = current_level
        for i in range(1, len(sorted_nums)):
            # If the difference is within the limit, assign to the same level
            if sorted_nums[i] - levels[current_level][-1] <= limit:
                levels[current_level].append(sorted_nums[i])
            else:
                # Otherwise, start a new level
                current_level += 1
                levels[current_level].append(sorted_nums[i])
            # Map element to its level
            level_map[sorted_nums[i]] = current_level
        # Rebuild the original array
        for i in range(len(nums)):
            # Replace with the smallest number in its level
            nums[i] = levels[level_map[nums[i]]].popleft()
        return nums
