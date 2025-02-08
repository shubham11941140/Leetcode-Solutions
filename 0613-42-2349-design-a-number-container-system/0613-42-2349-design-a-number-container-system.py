class NumberContainers:

    def __init__(self):
        self.m = {}
        self.d = {}
        
    def change(self, index: int, number: int) -> None:
        if index in self.m and self.m[index] == number: 
            return
        self.m[index] = number
        self.d.setdefault(number, [])
        heappush(self.d[number], index)     
        
    def find(self, number: int) -> int:
        if number not in self.d: 
            return -1
        while self.d[number] and self.m.get(self.d[number][0]) != number:
            heappop(self.d[number])
        return self.d[number][0] if self.d[number] else -1
        
# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)