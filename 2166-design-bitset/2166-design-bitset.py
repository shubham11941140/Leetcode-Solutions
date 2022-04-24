class Bitset:

    def __init__(self, size: int):
        self.bit = ["0"] * size
        self.fbit = ["1"] * size
        self.size = size
        self.c = 0
        
    def fix(self, idx: int) -> None:
        if self.bit[idx] == "0":
            self.bit[idx] = "1"
            self.fbit[idx] = "0"
            self.c += 1
        
    def unfix(self, idx: int) -> None:
        if self.bit[idx] == "1":
            self.bit[idx] = "0"
            self.fbit[idx] = "1"
            self.c -= 1        

    def flip(self) -> None:
        '''
        for i in range(self.size):
            if self.bit[i] == "0":
                self.bit[i] = "1"
            else:
                self.bit[i] = "0"
        '''
        self.bit, self.fbit = self.fbit, self.bit
        self.c = self.size - self.c
        
    def all(self) -> bool:
        return self.c == self.size        

    def one(self) -> bool:
        return self.c > 0        

    def count(self) -> int:
        return self.c        

    def toString(self) -> str:
        return ''.join(self.bit)
        
# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()