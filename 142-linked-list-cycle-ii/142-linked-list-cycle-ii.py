# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow and fast pointer
        slow = head
        fast = head
        if head is None or head.next is None:
            return None         
        while slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next            
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

