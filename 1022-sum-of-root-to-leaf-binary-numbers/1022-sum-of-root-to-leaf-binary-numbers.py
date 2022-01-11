class Solution:    
        
    def dfs(self, node, path):
        if not node: return 0
        path = (path << 1) + node.val			
        if not node.left and not node.right:
            return path            
        return self.dfs(node.left, path) + self.dfs(node.right, path)        
    
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
        