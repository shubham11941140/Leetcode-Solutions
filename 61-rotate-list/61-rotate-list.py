# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def listlen(self, a):
        c = 0
        while a is not None:
            c += 1
            a = a.next
        return c
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:        
        l = self.listlen(head)
        if not l:
            return head
        k = k % l
        if not head or not k or l == 1:
            return head        
        d = head     
        for i in range(l - k - 1):
            d = d.next
        f = d.next
        d.next = None        
        v = f
        while v is not None and v.next is not None:
            v = v.next
        v.next = head
        return f
            