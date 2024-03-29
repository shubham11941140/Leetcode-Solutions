# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @staticmethod
    def toarr(head):
        a = []
        while head is not None:
            a.append(head.val)
            head = head.next
        return a

    def atobst(self, a):
        if not a:
            return
        n = len(a) // 2
        return TreeNode(a[n], self.atobst(a[:n]), self.atobst(a[n + 1:]))

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        a = self.toarr(head)
        if not a:
            return None
        return self.atobst(a)
