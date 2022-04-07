class MyHashSet:

    def __init__(self):
        self.h = []        

    def add(self, key: int) -> None:
        if key not in self.h:
            self.h.append(key)        

    def remove(self, key: int) -> None:
        if key in self.h:
            self.h.remove(key)
        
    def contains(self, key: int) -> bool:
        return key in self.h
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)