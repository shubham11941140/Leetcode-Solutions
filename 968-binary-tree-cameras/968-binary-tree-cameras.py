# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, node: TreeNode) -> int:
        
        if not node: return 0
        val = self.dfs(node.left) + self.dfs(node.right)
    
        if val == 0: return 3
        if val < 3: return 0
        
        self.res += 1
        
        return 1    
    
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        #res = 0
        #def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0


        
        return self.res + 1 if self.dfs(root) > 2 else self.res        
        