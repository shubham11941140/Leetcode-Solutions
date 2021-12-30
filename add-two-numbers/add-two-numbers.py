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
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        a = l1
        b = l2
        ans = []
        c = 0
        while a is not None and b is not None:
            s = a.val + b.val + c
            ans.append(s % 10)
            c = int(s > 9)
            a = a.next
            b = b.next 
            
        while a is not None:
            s = a.val + c
            ans.append(s % 10)
            c = int(s > 9)
            a = a.next    
            
        while b is not None:
            s = b.val + c
            ans.append(s % 10)
            c = int(s > 9)
            b = b.next             
            
        if c:
            ans.append(1)

        r = None
        for i in reversed(range(len(ans))):
            r = self.insert(r, ans[i])
        return r
        