class MyHashMap:

    def __init__(self):
        self.h = dict()

    def put(self, key: int, value: int) -> None:
        self.h[key] = value

    def get(self, key: int) -> int:
        return self.h[key] if key in self.h else -1

    def remove(self, key: int) -> None:
        if key in self.h:
            del self.h[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
