# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.a = self.toarr(head)
        self.l = len(self.a)    
        
    def toarr(self, root):
        a = []
        while root is not None:
            a.append(root.val)
            root = root.next
        return a        

    def getRandom(self) -> int:
        return self.a[randint(0, self.l - 1)]        
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()