# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def insert(self, root, num):        
        temp = ListNode()
        temp.val = num
        temp.next = root
        root = temp
        return root
    
    def tolist(self, a):
        root = None
        for i in reversed(range(len(a))):
            root = self.insert(root, a[i])
        return root
            
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        while head is not None:            
            check = head.val
            c = 0
            while head is not None and check == head.val:
                c += 1
                head = head.next
            if c == 1:
                a.append(check)
        return self.tolist(a)
        