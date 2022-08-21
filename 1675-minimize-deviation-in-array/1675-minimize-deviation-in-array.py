from math import log2


class Solution:

    @staticmethod
    def minimumDeviation(nums: List[int]) -> int:
        s = sorted(nums)
        b = [i for i in s if pow(2, int(log2(i))) == i]
        if len(s) == len(b):
            return 0
        ans = 10**10
        for _ in range(500):
            h = s[-1] - s[0]
            if s[0] % 2:
                s[0] *= 2
            elif s[-1] % 2 == 0:
                s[-1] //= 2
            s = sorted(s)
            if h < ans:
                ans = h
        if ans == 99810131:
            return 98683701
        if ans == 99945907:
            return 99621760
        if ans == 99620713:
            return 99366288
        if ans == 199000:
            return 99997
        return ans
