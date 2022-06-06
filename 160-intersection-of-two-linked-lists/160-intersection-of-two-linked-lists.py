# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def toarr(self, head):
        a = []
        while head:
            a.append(head.val)
            head = head.next
        return a
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = self.toarr(headA)[::-1]
        b = self.toarr(headB)[::-1]
        #print(a, b)
        la = len(a)
        lb = len(b)
        
        ha = headA
        hb = headB
        
        if lb > la:
            while lb > la:
                hb = hb.next
                lb -= 1
        if la > lb:
            while la > lb:
                ha = ha.next
                la -= 1
        
        # Guarantee that la = lb
        assert la == lb
        
        while la and lb:
            if ha == hb:
                return ha
            ha = ha.next
            hb = hb.next
            la -= 1
            lb -= 1
        return None

                
        
        
        