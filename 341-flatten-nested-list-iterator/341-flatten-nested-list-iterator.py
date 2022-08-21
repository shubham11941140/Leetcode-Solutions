
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.ans = []
        for i in nestedList:
            self.traverse(i)
        self.idx = -1
        self.l = len(self.ans)      
        
    def traverse(self, nested_list):
        if nested_list.isInteger():
            self.ans.append(nested_list.getInteger())
        else:
            for i in nested_list.getList():
                self.traverse(i)                
    
    def next(self) -> int:
        self.idx += 1
        return self.ans[self.idx]             
    
    def hasNext(self) -> bool:
        return self.idx + 1 < self.l
            
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())