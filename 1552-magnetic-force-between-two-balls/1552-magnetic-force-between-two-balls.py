class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()  # Sort the basket positions
        left, right = 1, position[-1] - position[0]  # Initialize search range

        while left < right:
            mid = (left + right + 1) // 2
            if self.can_place_balls(position, mid, m):
                left = mid
            else:
                right = mid - 1

        return left

    def can_place_balls(self, position: List[int], min_distance: int, m: int) -> bool:
        initial = 1
        prev = position[0]

        for i in range(1, len(position)):
            if position[i] - prev >= min_distance:
                initial += 1
                prev = position[i]

        return initial >= m        