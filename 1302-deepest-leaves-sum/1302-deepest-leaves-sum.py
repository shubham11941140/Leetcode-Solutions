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
    
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = [(root, 0)]
        h = self.height(root)
        ans = 0
        while q:
            root, level = q.pop(0)
            if level == h - 1:
                ans += root.val
            if root.left:
                q.append((root.left, level + 1))
            if root.right:
                q.append((root.right, level + 1))
        return ans
