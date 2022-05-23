class Skiplist:

    def __init__(self):
        self.d = dict()        

    def search(self, target: int) -> bool:
        return target in self.d
        

    def add(self, num: int) -> None:
        if num in self.d:
            self.d[num] += 1
        else:
            self.d[num] = 1
        

    def erase(self, num: int) -> bool:
        if not self.search(num):
            return False
        self.d[num] -= 1
        if not self.d[num]:
            del self.d[num]
        return True
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)