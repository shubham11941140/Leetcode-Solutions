class Solution:
    def check(self, num, dig): 
        c = 3
        digits = dig.copy()
        for i in num:
            if int(i) in digits:
                digits.remove(int(i))
                c -= 1
            else:
                return False
        return not c

    def totalNumbers(self, digits: List[int]) -> int:
        return len([i for i in range(100, 1000, 2) if self.check(str(i), digits)])