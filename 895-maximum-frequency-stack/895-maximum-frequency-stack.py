class FreqStack:

    def __init__(self):
        self.s = []
        self.m = {}
        self.max = 0
        self.l = 0

    def push(self, val: int) -> None:
        self.s.append(val)
        self.m[val] = self.m[val] + 1 if val in self.m else 1
        self.max = max(self.m.values())
        self.l += 1

    def pop(self) -> int:
        idx = -1
        for i in reversed(range((self.l))):
            if self.m[self.s[i]] == self.max:
                idx = i
                break
        # Remove and update
        val = self.s[idx]
        self.m[val] -= 1
        self.max = max(self.m.values())
        self.s.pop(idx)
        self.l -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
