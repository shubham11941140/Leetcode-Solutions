# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    @staticmethod
    def isPalindrome(head: Optional[ListNode]) -> bool:
        a = []
        while head is not None:
            a.append(head.val)
            head = head.next
        return a == a[::-1]
