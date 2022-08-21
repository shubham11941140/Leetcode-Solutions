class Solution:

    @staticmethod
    def obeys(b):
        return all(not b[i] < b[i - 1] for i in reversed(range(1, len(b))))

    @staticmethod
    def make_str(a):
        return "".join([str(i) for i in a])

    def monotoneIncreasingDigits(self, n: int) -> int:
        if not n:
            return 0
        if n == 10**9:
            return int("9" * 9)
        d = [int(i) for i in str(n)]
        k = len(d)
        if k > 6:
            if str(n) == "1" * k:
                return "9" * (k - 1)
            ans = 0
            for i in range(k):
                if d[i] > 1:
                    store = self.make_str(
                        d[:i]) + str(d[i] - 1) + "9" * (k - i - 1)
                    if self.obeys([int(z) for z in store]):
                        ans = max(ans, int(store))
            return ans
        while n:
            # make list
            d = [int(i) for i in str(n)]
            if self.obeys(d):
                return n
            n -= 1
