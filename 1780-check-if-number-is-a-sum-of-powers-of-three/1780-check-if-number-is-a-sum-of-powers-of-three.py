class Solution:

    def subset(self, a, temp, idx):
        if idx == len(a):
            self.ans.append(temp.copy())
            return
        self.subset(a, temp + [a[idx]], idx + 1)
        self.subset(a, temp, idx + 1)

    def checkPowersOfThree(self, n: int) -> bool:
        x = 1
        a = []
        while x <= 10**7:
            a.append(x)
            x *= 3
        temp = []
        idx = 0
        self.ans = []
        self.subset(a, temp, idx)
        # print(self.ans)
        # print(len(self.ans))
        b = [sum(i) for i in self.ans]
        # print(b)
        return n in b
