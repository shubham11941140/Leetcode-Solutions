class MyStack:

    def __init__(self):
        self.a = []        

    def push(self, x: int) -> None:
        self.a.append(x)
        
    def pop(self) -> int:
        return self.a.pop()   

    def top(self) -> int:        
        return self.a[-1]
        
    def empty(self) -> bool:
        return not self.a
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()