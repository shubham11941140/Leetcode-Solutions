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
    
    def print(self, l):
        h = 0
        while l is not None:
            h += 1
            if h == 10:
                break
            print(l.val)
            l = l.next
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        l = self.listlen(head)
        if not l:
            return head

        k = k % l
        if not head or not k or l == 1:
            return head        

        print(l)
        r = head
        m = head
        '''
        while head.next is not None:
            head = head.next
        head.next = r
        '''
        self.print(r)
        d = head     
        for i in range(l - k - 1):
            d = d.next
        print(27)
        print("D", d.val)
        g = d.next
        f = d.next
        print(g)
        d.next = None
        self.print(head)
        print(46)
        self.print(f)
        
        v = f
        while v is not None and v.next is not None:
            v = v.next
        v.next = head
        return f
            
        
        
        
        '''
        while g.next is not None:
            g = g.next
        g.next = r
        '''

        '''
        c = 0
        while d is not None:
            c += 1
            if c == 20:
                break
            print(d.val)
            d = d.next
        '''