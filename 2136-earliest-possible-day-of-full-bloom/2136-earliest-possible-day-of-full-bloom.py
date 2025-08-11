class Solution:

    def earliestFullBloom(self, plantTime: List[int],
                          growTime: List[int]) -> int:
        ans = 0
        for g, p in sorted(zip(growTime, plantTime)):
            ans = max(ans, g) + p
        return ans
