# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def listlen(self, a):
        c = 0
        while a is not None:
            c += 1
            a = a.next
        return c    
    
    def insert(self, root, k):
        temp = ListNode()
        temp.val = k
        temp.next = root
        root = temp
        return root
                    
    def atol(self, a): 
        root = None
        for i in a[::-1]:
            root = self.insert(root, i)
        return root
    
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l = self.listlen(head)
        c = l // k
        e = l % k
        adj = [[] for i in range(k)]
        for i in range(k):
            if e:
                for j in range(c + 1):
                    adj[i].append(head.val)
                    head = head.next
                e -= 1
            else:
                for j in range(c):
                    adj[i].append(head.val)
                    head = head.next  
        print(adj)
        f = []
        for i in adj:
            f.append(self.atol(i))
        return f
                    
            
        
        