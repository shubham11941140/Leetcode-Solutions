# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        if head is None or head.next is None:
            return False       
        while slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next            
            if slow == fast:
                return True
