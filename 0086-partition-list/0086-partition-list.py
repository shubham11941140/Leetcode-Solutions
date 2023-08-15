# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        a, b = [], []
        while head is not None:
            if head.val < x:
                a.append(head.val)
            else:
                b.append(head.val)            
            head = head.next
        r = None
        for i in reversed(a + b):
            temp = ListNode(i)
            temp.next =r
            r = temp
        return r