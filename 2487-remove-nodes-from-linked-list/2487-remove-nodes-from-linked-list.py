# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return head.next and (setattr(head, 'next', q := self.removeNodes(head.next)), q)[head.val < q.val] or head      