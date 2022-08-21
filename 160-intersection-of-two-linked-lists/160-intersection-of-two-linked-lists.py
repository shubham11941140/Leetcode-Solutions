# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    @staticmethod
    def length(head):
        c = 0
        while head:
            c += 1
            head = head.next
        return c

    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> Optional[ListNode]:

        la = self.length(headA)
        lb = self.length(headB)

        if lb > la:
            while lb > la:
                headB = headB.next
                lb -= 1

        if la > lb:
            while la > lb:
                headA = headA.next
                la -= 1

        while la and lb:

            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next
            la -= 1
            lb -= 1

        return None
