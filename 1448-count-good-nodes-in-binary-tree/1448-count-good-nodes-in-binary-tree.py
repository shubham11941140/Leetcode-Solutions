# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, root, curr):
        if not root:
            return
        if root.val >= curr:
            self.ans += 1
            curr = max(curr, root.val)
        self.dfs(root.left, curr)
        self.dfs(root.right, curr)
        
        
    
    
    def goodNodes(self, root: TreeNode) -> int:        
        self.ans = 0
        self.dfs(root, root.val)
        return self.ans
        