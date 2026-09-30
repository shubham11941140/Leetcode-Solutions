class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        cur = 1
        for bracket in seq:
            ans.append((1 - cur) if bracket == '(' else cur)
            cur ^= 1
        return ans        