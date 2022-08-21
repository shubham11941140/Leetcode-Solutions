from math import ceil


class Solution:

    def condition(self, mid, a):
        n = len(a)
        i = 0
        c = 0
        while i < n:
            s = 0
            while i < n and s + a[i] <= mid:
                s += a[i]
                i += 1
            c += 1
            if c > n:
                break
        return c

    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        left = max(nums)
        right = sum(nums)
        if self.condition(left, nums) < m:
            return left
        for i in range(left, left + 1000 + 1):
            if self.condition(i, nums) == m:
                return i
        while left <= right:
            mid = ceil((left + right) / 2)
            c = self.condition(mid, nums)
            if c > m:
                left = mid
            elif c <= m:
                if c == m and self.condition(mid - 1, nums) != m:
                    return mid
                right = mid
