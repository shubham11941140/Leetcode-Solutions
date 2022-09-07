# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def po(self, root, a):
        if not root:
            return
        a.append(str(root.val))
        a.append('(')
        self.po(root.left, a)
        a.append(')')
        a.append('(')
        self.po(root.right, a)
        a.append(')')
        
    def rec(self, root):
        if not root:
            return ''
        # Root exists   
        #print(root)
        if not root.left and not root.right:
            #print(27)
            return str(root.val)
        if root.left and not root.right:  
            #print(30)
            return str(root.val) + '(' + self.rec(root.left) + ')'
        if not root.left and root.right:
            #print(33)
            return str(root.val) + '()' + '(' + self.rec(root.right) + ')'
        if root.left and root.right:
            #print(36)
            return str(root.val) + '(' + self.rec(root.left) + ')' + '(' + self.rec(root.right) + ')'
        
    def tree2str(self, root: Optional[TreeNode]) -> str:
        s = self.rec(root)
        print("S", s)
        return s