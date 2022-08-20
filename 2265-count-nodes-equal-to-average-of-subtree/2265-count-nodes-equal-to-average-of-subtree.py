# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def comp(self, root):
        if not root:
            return
        self.ans1 += root.val
        self.ans2 += 1
        self.comp(root.left)
        self.comp(root.right)
        
    def avg(self, root):
        if not root:
            return
        self.ans1 = 0
        self.ans2 = 0
        self.comp(root)
        if self.ans2 and root.val == (self.ans1 // self.ans2):
            self.c += 1          
        self.avg(root.left)          
        self.avg(root.right)
        
                    
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.c = 0
        self.avg(root)
        return self.c
        