# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    @staticmethod
    def getlen(head):
        l = 0
        while head is not None:
            l += 1
            head = head.next
        return l

    def removeNthFromEnd(self, head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        l = self.getlen(head)
        if l == 1:
            return None
        if l == n:
            head = head.next
            return head
        c = 0
        root = head
        while head is not None:
            c += 1
            if c == l - n:
                head.next = head.next.next
            head = head.next
        return root
