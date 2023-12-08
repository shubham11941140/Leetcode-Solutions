# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        l = root.left
        r = root.right
        s = str(root.val)
        if not l and not r:
            return s
        if l and not r:  
            return s + '(' + self.tree2str(l) + ')'
        if not l and r:
            return s + '()' + '(' + self.tree2str(r) + ')'
        if l and r:
            return s + '(' + self.tree2str(l) + ')' + '(' + self.tree2str(r) + ')'
      