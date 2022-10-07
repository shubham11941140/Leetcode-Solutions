from collections import Counter

class MyCalendarTwo:

    def __init__(self):
        self.d = Counter()
        
    def book(self, start: int, end: int) -> bool:
        self.d[start] += 1
        self.d[end] -= 1
        active = ans = 0
        for x in sorted(self.d):
            active += self.d[x]
            if active >= 3:
                self.d[start] -= 1
                self.d[end] += 1
                return False
        return True        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)