# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def height(self, root) -> int:
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
    
    # traverse the tree to get nodes at deepest level
    def bfs_level(self, root) -> list:
        level = 0
        q = [(root, level)]
        h = self.height(root)
        ans = []
        while q:
            root, level = q.pop(0)
            if level == h - 1:
                ans.append(root.val)
            if root.left:
                q.append((root.left, level + 1))
            if root.right:
                q.append((root.right, level + 1))
        return ans           
    
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans = self.bfs_level(root)
        return sum(ans)