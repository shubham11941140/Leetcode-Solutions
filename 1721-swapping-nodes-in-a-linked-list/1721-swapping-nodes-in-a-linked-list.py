# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = 0
        root = head
        while root is not None:
            l += 1
            root = root.next
        root = head
        c = 0
        b1 = -1
        b2 = -1
        while root is not None:
            c += 1
            if c == k:
                b1 = root.val
            if c == l - k + 1:
                b2 = root.val
            root = root.next
        b1, b2 = b2, b1
        root = head
        c = 0
        while root is not None:
            c += 1
            if c == k:
                root.val = b1
            if c == l - k + 1:
                root.val = b2
            root = root.next        
        return head
        
