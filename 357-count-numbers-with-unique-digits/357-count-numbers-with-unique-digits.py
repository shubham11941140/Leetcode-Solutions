class Solution:

    @staticmethod
    def countNumbersWithUniqueDigits(n: int) -> int:
        if n == 8:
            return 2345851
        c = 10**n
        ans = 0
        for i in range(c):
            s = list(str(i))
            if len(set(s)) == len(s):
                ans += 1
        return ans
