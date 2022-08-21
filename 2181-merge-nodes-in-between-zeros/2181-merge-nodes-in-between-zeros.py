# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        while head is not None:
            a.append(head.val)
            head = head.next
        n = len(a)
        z = [i for i in range(n) if not a[i]]
        lz = len(z)
        b = [sum([a[k] for k in range(z[i], z[i + 1])]) for i in range(lz - 1)]
        self.r = None
        for i in b[::-1]:
            t = ListNode(i)
            t.next = self.r
            self.r = t
        return self.r
