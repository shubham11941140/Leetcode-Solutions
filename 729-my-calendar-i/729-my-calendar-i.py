class MyCalendar:

    def __init__(self):
        self.c = []
        
    def book(self, start: int, end: int) -> bool:
        for s, e in self.c:
            if (start >= s and end < e) or s <= start < e or end > s >= start:
                return False
        self.c.append((start, end))
        return True
            
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)