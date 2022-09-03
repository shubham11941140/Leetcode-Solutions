class Solution:

    def rec(self, a):
        if len(a) == self.n:
            self.ans.append(int("".join([str(x) for x in a])))
            return
        prev = a[-1]
        for i in [prev + self.k, prev - self.k]:
            if 0 <= i <= 9:
                self.rec(a + [i])

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.n = n
        self.k = k
        self.ans = []
        for i in range(1, 10):
            self.rec([i])
        return list(set(self.ans))
