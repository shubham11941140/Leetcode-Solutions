class MyLinkedList:

    def __init__(self):
        self.a = []        
    
    def get(self, index: int) -> int:
        print(self.a)
        print(index, len(self.a))
        if 0 <= index < len(self.a):
            return self.a[index]
        return -1
        
    def addAtHead(self, val: int) -> None:
        self.a.insert(0, val)
        
    def addAtTail(self, val: int) -> None:
        self.a.append(val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        print(self.a)
        print(index, val)
        if 0 <= index <= len(self.a):        
            self.a.insert(index, val)
        print(self.a)
                
    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < len(self.a):        
            self.a.pop(index)        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)