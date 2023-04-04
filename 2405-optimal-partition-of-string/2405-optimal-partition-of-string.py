class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        ss = ""
        for i in s:
            if i not in ss:
                ss += i
            else:
                ans += 1
                ss = i
        return ans + 1
