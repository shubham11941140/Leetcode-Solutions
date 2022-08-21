class Solution:

    def isint(self, a):
        try:
            return int(a)
        except:
            return -1

    def check(self, a):
        n = len(a)
        return len(set(a)) == n and a == sorted(a)

    def areNumbersAscending(self, s: str) -> bool:
        return self.check(
            [int(i) for i in s.split(" ") if self.isint(i) != -1])
