class MyCircularDeque:

    def __init__(self, k: int):
        self.a = []
        self.l = k
        
    def insertFront(self, value: int) -> bool:
        if len(self.a) < self.l:
            self.a = [value] + self.a
            return True
        return False        

    def insertLast(self, value: int) -> bool:
        if len(self.a) < self.l:
            self.a.append(value)
            return True
        return False            

    def deleteFront(self) -> bool:
        if self.a:
            self.a.pop(0)
            return True
        return False
        
    def deleteLast(self) -> bool:
        if self.a:
            self.a.pop()
            return True
        return False
        
    def getFront(self) -> int:
        return self.a[0] if self.a else -1

    def getRear(self) -> int:
        return self.a[-1] if self.a else -1        

    def isEmpty(self) -> bool:
        return not self.a        

    def isFull(self) -> bool:
        return len(self.a) == self.l


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()