# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def insert(self, i):
        t = ListNode(i)
        t.next = self.r
        self.r = t

    def insertionSortList(self,
                          head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        while head is not None:
            a.append(head.val)
            head = head.next
        self.r = None
        for i in sorted(a, reverse=True):
            self.insert(i)
        return self.r
