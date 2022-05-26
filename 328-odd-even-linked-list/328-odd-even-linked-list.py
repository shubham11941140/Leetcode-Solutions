# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def toarr(self, head):
        a = []
        while head:
            a.append(head.val)
            head = head.next
        return a
    
    def insert(self, root, val):
        temp = ListNode()
        temp.val = val
        temp.next = root
        root = temp
        return root
    
    def atol(self, a):
        root = None
        for i in reversed(a):
            root = self.insert(root, i)
        return root
    
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toarr(head)
        if not a:
            return None
        n = len(a)
        b = []
        for i in range(n):
            if not (i % 2):
                b.append(a[i])
        for i in range(n):
            if i % 2:
                b.append(a[i])
        print(b)
        return self.atol(b)
        
        