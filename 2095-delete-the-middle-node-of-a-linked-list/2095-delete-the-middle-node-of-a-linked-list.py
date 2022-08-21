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

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = self.getlen(head)
        if l == 1:
            return None
        c = 0
        root = head
        while head is not None:
            c += 1
            if c == l // 2:
                head.next = head.next.next
            head = head.next
        return root
