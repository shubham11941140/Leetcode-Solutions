class Solution:
    def check(self, num, dig):
        v = [int(i) for i in str(num)]
        c = len(v)
        digits = dig.copy()
        for i in v:
            if i in digits:
                digits.remove(i)
                c -= 1
            else:
                return False
        return c == 0

    def totalNumbers(self, digits: List[int]) -> int:
        return len([i for i in range(100, 1000, 2) if self.check(i, digits)])