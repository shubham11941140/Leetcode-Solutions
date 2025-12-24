class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = sum(apple)
        c = 0
        l = 0
        for i in sorted(capacity, reverse = True):
            c += i
            l += 1
            print(c, l)
            if c >= s:
                return l

