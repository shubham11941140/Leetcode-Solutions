# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r = head
        while head is not None:
            c = head
            print(c.val)
            while head is not None and head.val == c.val:
                head = head.next
            c.next = head
            #head = head.next
        return r
            
            
        