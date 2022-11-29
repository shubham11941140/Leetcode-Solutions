class RandomizedCollection:

    def __init__(self):
        self.a = []        
        
    def insert(self, val: int) -> bool:
        flag = val not in self.a
        self.a.append(val)
        return flag
        
    def remove(self, val: int) -> bool:
        if val not in self.a:
            return False
        self.a.remove(val)
        return True      

    def getRandom(self) -> int:
        return random.choice(self.a)
        
# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()