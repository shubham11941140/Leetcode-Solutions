class Solution:

    @staticmethod
    def maxArea(height: List[int]) -> int:
        # Find farthest greater element on left and right
        l = 0
        r = len(height) - 1
        ans = -1
        while l <= r:
            area = (r - l) * min(height[l], height[r])
            ans = max(ans, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans
