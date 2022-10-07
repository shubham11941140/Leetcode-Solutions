from collections import Counter


class MyCalendarThree:

    def __init__(self):
        self.d = Counter()

    def book(self, start: int, end: int) -> int:
        self.d[start] += 1
        self.d[end] -= 1
        active = ans = 0
        for x in sorted(self.d):
            active += self.d[x]
            if active > ans:
                ans = active
        return ans


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
