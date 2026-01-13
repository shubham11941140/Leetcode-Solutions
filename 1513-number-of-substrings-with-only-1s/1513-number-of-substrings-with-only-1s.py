class Solution:

    def numSub(self, s: str) -> int:
        ans = 0
        count1 = 0
        for ch in s:
            if ch == "1":
                count1 += 1
                ans += count1
            else:
                count1 = 0
        return ans % (10**9 + 7)
