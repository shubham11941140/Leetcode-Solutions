class FrontMiddleBackQueue:

    def __init__(self):
        self.a = []                

    def pushFront(self, val: int) -> None:
        self.a = [val] + self.a        

    def pushMiddle(self, val: int) -> None:     
        k = len(self.a)
        if k % 2 == 0:
            idx = (k - 1) // 2
            self.a = self.a[:idx + 1] + [val] + self.a[idx + 1:]
        else:
            idx = (k - 1) // 2
            self.a = self.a[:idx] + [val] + self.a[idx:]                    

    def pushBack(self, val: int) -> None:
        self.a.append(val)        

    def popFront(self) -> int:
        return self.a.pop(0) if self.a else -1                            

    def popMiddle(self) -> int:
        if len(self.a):
            k = len(self.a)
            idx = (k - 1) // 2
            return self.a.pop(idx)        
        return -1
        
    def popBack(self) -> int:
        return self.a.pop() if self.a else -1
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()