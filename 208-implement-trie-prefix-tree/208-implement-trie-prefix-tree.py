class Trie:

    def __init__(self):
        self.arr = [None] * 26
        self.end = False

    def insert(self, word: str) -> None:
        p = self
        for i, item in enumerate(word):
            idx = ord(item) - ord("a")
            if not p.arr[idx]:
                p.arr[idx] = Trie()
            p = p.arr[idx]
        p.end = True

    def search(self, word: str) -> bool:
        p = self
        for i, item in enumerate(word):
            idx = ord(item) - ord("a")
            if p.arr[idx] is None:
                return False
            p = p.arr[idx]
        return p.end

    def startsWith(self, prefix: str) -> bool:
        p = self
        for i, item in enumerate(prefix):
            idx = ord(item) - ord("a")
            if not p.arr[idx]:
                return False
            p = p.arr[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
