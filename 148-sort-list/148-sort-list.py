# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    @staticmethod
    def insert(root, b):
        newnode = ListNode()
        newnode.val = b
        newnode.next = root
        root = newnode
        return root

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        b = []
        while head is not None:
            b.append(head.val)
            head = head.next
        b.sort()
        root = None
        for i in b[::-1]:
            root = self.insert(root, i)
        return root
