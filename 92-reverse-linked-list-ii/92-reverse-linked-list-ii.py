# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def insert(self, root, item):
        temp = ListNode(0)
        temp.val = item
        temp.next = root
        root = temp
        return root
    
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        r = head
        a = []
        while r is not None:
            a.append(r.val)
            r = r.next
        f = a[left - 1: right]
        b = a[:left - 1] + f[::-1] + a[right:]
        print(b)
        root = None
        for i in reversed(b):
            root = self.insert(root, i)
        return root
        
        