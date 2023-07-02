class Solution:

    def sub(self, req, idx, curr):
        if idx == self.r:
            self.a.append(curr)
            return
        self.sub(req, idx + 1, curr + [req[idx]])
        self.sub(req, idx + 1, curr)

    def satisfy(self, n, a):
        b = [0] * n
        for i in a:
            b[i[0]] -= 1
            b[i[1]] += 1
        if b.count(0) == n:
            return len(a)
        return 0

    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.r = len(requests)
        self.a = []
        self.sub(requests, 0, [])
        # print(self.a)
        print(len(self.a))
        m = 0
        for i in self.a:
            # Check satisfy
            c = self.satisfy(n, i)
            m = max(m, c)
        return m
