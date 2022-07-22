# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def insert(self, item):
        temp = ListNode(item)
        temp.next = self.root
        self.root = temp
    
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        a = []
        b = []
        while head is not None:
            if head.val < x:
                a.append(head.val)
            else:
                b.append(head.val)            
            head = head.next
        print(a, b)
        c = a + b
        print(c)
        self.root = None
        for i in reversed(c):
            self.insert(i)
        return self.root