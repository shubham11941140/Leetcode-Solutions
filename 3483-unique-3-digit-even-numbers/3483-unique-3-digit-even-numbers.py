class Solution:
    def check(self, num, dig):
        v = [int(i) for i in str(num)]
        c = len(v)
        #print(v, dig)
        digits = dig.copy()

        for i in v:
            if i in digits:
                digits.remove(i)
                c -= 1
        #print(c)
        return c == 0

    def totalNumbers(self, digits: List[int]) -> int:
        return len([i for i in range(100, 1000) if self.check(i, digits) and i % 2 == 0])
            
        