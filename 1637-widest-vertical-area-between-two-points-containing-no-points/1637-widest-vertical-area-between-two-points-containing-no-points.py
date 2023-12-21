class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # Sort the points based on x-coordinate
        points.sort(key = lambda x: x[0])

        # Initialize max_width to 0
        max_width = 0

        # Iterate over the sorted points
        for i in range(1, len(points)):
            # Update max_width if the difference between current and previous point is greater
            max_width = max(max_width, points[i][0] - points[i-1][0])

        # Return the maximum width
        return max_width        