class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        t = s + s
        ans = n
        mis0 = 0
        for i in range(2 * n):
            expected0 = '0' if i % 2 == 0 else '1'
            if t[i] != expected0:
                mis0 += 1
            if i >= n:
                left = i - n
                exp_left = '0' if left % 2 == 0 else '1'
                if t[left] != exp_left:
                    mis0 -= 1
            if i >= n - 1: 
                ans = min(ans, min(mis0, n - mis0))
        return ans        