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
    
    def toarr(self, head):
        a = []
        while head is not None:
            a.append(head.val)
            head = head.next
        return a
    
    def atobst(self, a):
        if not a:
            return
        print(a)
        n = len(a) // 2
        print(a[:n])
        print(a[n])
        print(a[n + 1:])
        return TreeNode(a[n], self.atobst(a[:n]), self.atobst(a[n + 1:]))
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        a = self.toarr(head)
        print(a)
        if not a:
            return None 
        return self.atobst(a)

        
        
        '''
        n = len(a)
        i = n // 2
        t = TreeNode(a[i])
        u = t
        root = t
        for j in reversed(range(i)):
            t.left = TreeNode(a[j])
            t = t.left
        for j in range(i + 1, n):
            u.right = TreeNode(a[j])
            u = u.right
        #print("F", v)
        return root
        '''
        