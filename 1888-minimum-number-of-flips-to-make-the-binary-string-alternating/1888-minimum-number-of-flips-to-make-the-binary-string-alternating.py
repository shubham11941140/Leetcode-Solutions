class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        t = s + s
        ans = n
        mis0 = 0
        for i in range(2 * n):
            if t[i] != str(i % 2):
                mis0 += 1
            if i >= n:
                left = i - n
                if t[left] != str(left % 2):
                    mis0 -= 1
            if i >= n - 1: 
                ans = min(ans, min(mis0, n - mis0))
        return ans        