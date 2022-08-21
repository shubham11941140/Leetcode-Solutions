class Solution:

    @staticmethod
    def isint(a):
        try:
            return int(a)
        except:
            return -1

    @staticmethod
    def check(a):
        n = len(a)
        return len(set(a)) == n and a == sorted(a)

    def areNumbersAscending(self, s: str) -> bool:
        return self.check(
            [int(i) for i in s.split(" ") if self.isint(i) != -1])
