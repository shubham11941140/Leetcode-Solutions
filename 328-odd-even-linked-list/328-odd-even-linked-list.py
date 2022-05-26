# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def toarr(self, head):
        a = []
        while head:
            a.append(head.val)
            head = head.next
        return a
    
    def insert(self, root, val):
        temp = ListNode()
        temp.val = val
        temp.next = root
        root = temp
        return root
    
    def atol(self, a):
        root = None
        for i in reversed(a):
            root = self.insert(root, i)
        return root
    
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toarr(head)
        if not a:
            return None
        n = len(a)
        return self.atol([a[i] for i in range(0, n, 2)] + [a[i] for i in range(1, n, 2)])
        
        