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
    
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        while head is not None:
            a.append(head.val)
            head = head.next
        print(a)
        n = len(a)
        z = [i for i in range(n) if not a[i]]
        print(z)
        b = []
        for i in range(len(z) - 1):
            l, r = z[i], z[i + 1]
            s = sum([a[k] for k in range(l, r)])
            b.append(s)
        print(b)
        self.r = None
        for i in b[::-1]:
            self.insert(i)
        return self.r
                
            
        