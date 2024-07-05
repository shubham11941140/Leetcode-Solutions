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
        print(a)
        n = len(a)
        if n < 3:
            return [-1, -1]
        cp = []
        for i in range(1, n - 1):
            if a[i] > max(a[i - 1], a[i + 1]) or a[i] < min(a[i - 1], a[i + 1]):
                cp.append(i)
        print("CP", cp)
        if len(cp) < 2:
            return [-1, -1]
        maxd = cp[-1] - cp[0]
        mind = min([cp[i] - cp[i - 1] for i in range(1, len(cp))])
        return [mind, maxd]
