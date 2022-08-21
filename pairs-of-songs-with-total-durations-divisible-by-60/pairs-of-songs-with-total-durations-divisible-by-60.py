class Solution:

    @staticmethod
    def freq(a):
        d = {}
        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return d

    @staticmethod
    def con(a):
        return (a * (a - 1)) // 2

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n = len(time)
        for i in range(n):
            time[i] %= 60

        d = self.freq(time)
        ans = 0
        for i in range(61):
            if i not in d:
                d[i] = 0

        ans = 0
        for i in range(1, 30):
            rem = 60 - i
            val = d[i] * d[rem]
            ans += val
        ans += self.con(d[0]) + self.con(d[30])
        return ans
