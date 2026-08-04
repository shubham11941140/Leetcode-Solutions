# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return (
            0
            if not root
            else self.rangeSumBST(root.right, low, high)
            + self.rangeSumBST(root.left, low, high)
            + int(low <= root.val <= high) * root.val
        )
