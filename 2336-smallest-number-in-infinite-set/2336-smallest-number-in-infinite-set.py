class SmallestInfiniteSet:

    def __init__(self):
        self.a = [i for i in range(1, 5000)]
            
    def popSmallest(self) -> int:        
        return self.a.pop(0)        

    def addBack(self, num: int) -> None:
        if num not in self.a:
            self.a.append(num)
            self.a.sort()
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)