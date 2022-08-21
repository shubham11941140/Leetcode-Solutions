from random import choice


class RandomizedSet:

    def __init__(self):
        self.a = []

    def insert(self, val: int) -> bool:
        if val not in self.a:
            self.a.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.a:
            self.a.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.a)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
