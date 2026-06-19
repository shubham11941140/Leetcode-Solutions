# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseKGroup(self, head: Optional[ListNode],
                      k: int) -> Optional[ListNode]:
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                prev, curr = r, l
                for _ in range(k):
                    curr.next, prev, curr = prev, curr, curr.next
                jump.next, jump, l = prev, l, r
            else:
                return dummy.next
