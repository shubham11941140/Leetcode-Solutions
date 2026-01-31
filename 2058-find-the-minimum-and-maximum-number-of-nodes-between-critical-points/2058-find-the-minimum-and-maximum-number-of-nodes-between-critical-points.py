# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        n = len(a)
        if n < 3:
            return [-1, -1]
        cp = [
            i
            for i in range(1, n - 1)
            if a[i] > max(a[i - 1], a[i + 1]) or a[i] < min(a[i - 1], a[i + 1])
        ]
        return (
            [-1, -1]
            if len(cp) < 2
            else [min([cp[i] - cp[i - 1] for i in range(1, len(cp))]), cp[-1] - cp[0]]
        )
