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

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        a = []
        while head is not None:
            a.append(head.val)
            head = head.next
        self.root = None
        for i in reversed(a[:left - 1] + a[left - 1: right][::-1] + a[right:]):
            self.insert(i)
        return self.root


