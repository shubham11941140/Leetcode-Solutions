# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


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
