class Solution:

    def sn(self, r):
        return (r * (r + 1)) // 2

    def calc(self, m, ele):
        # print("M", m, ele)
        s = 0
        if ele >= m - 1:
            s = ((m * (m - 1)) // 2) + 1 * (ele - (m - 1))
        if ele < m - 1:
            rem = m - 1 - ele
            s = ((m * (m - 1)) // 2) - self.sn(rem)
        return s

    def help(self, n, idx, m):
        # Have idx elements before
        s1 = self.calc(m, idx)

        # n - idx - 1
        s2 = self.calc(m, n - 1 - idx)

        # print(s1, s2, m)

        return s1 + s2 + m

        nums = [1 for i in range(n)]
        nums[idx] = m
        val1 = nums[idx]
        val2 = nums[idx]
        for i in range(idx + 1, n):
            val1 -= 1
            if val1 <= 0:
                break
            nums[i] = val1
        for i in reversed(range(idx)):
            val2 -= 1
            if val2 <= 0:
                break
            nums[i] = val2
        if s1 + s2 + m != sum(nums):
            print(nums, m - 1, idx, n - 1 - idx)
            print(4111111111111, s1, s2, s1 + s2 + m, sum(nums))
        return sum(nums)

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l = 1
        r = maxSum
        c = 0
        while l <= r:
            c += 1
            if c > 100:
                break
            if r - l <= 100:
                for i in reversed(range(l, r + 1)):
                    if self.help(n, index, i) <= maxSum:
                        return i
            m = (l + r) // 2
            s = self.help(n, index, m)
            print(s, m)
            if s > maxSum:
                r = m
            if s <= maxSum:
                # call test
                if self.help(n, index, m + 1) > maxSum:
                    return m
                l = m
        return 0
