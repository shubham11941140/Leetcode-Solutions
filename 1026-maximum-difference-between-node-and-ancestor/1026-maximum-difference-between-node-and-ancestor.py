# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        diff = 0

        def dfs(n):
            nonlocal diff
            vals = [n.val]
            if n.left:
                vals.extend(dfs(n.left))
            if n.right:
                vals.extend(dfs(n.right))
            mn, mx = min(vals), max(vals)
            diff = max(diff, abs(n.val - mn), abs(n.val - mx))
            return (mn, mx)

        dfs(root)
        return diff
