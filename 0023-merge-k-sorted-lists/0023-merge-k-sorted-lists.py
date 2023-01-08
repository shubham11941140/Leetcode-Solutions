# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def toarray(self, a):
        b = []
        while a is not None:
            b.append(a.val)
            a = a.next
        return b
    
    def insert(self, root, item):
        temp = ListNode()
        temp.val = item
        temp.next = root
        root = temp
        return root
    
    def tolist(self, a):
        root = None
        for i in a[::-1]:
            root = self.insert(root, i)
        return root      
                
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:              
        d = []
        for i in lists:
            d += self.toarray(i)
        return self.tolist(sorted(d))
            
        
        
        
        
        
        
        
        
        