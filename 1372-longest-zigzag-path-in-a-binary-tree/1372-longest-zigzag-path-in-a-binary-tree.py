# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, direction):
            if not node:
                return 0
            left = dfs(node.left, 0)
            right = dfs(node.right, 1)
            self.ans = max(self.ans, left, right)
            if direction == 0:
                return right + 1
            else:
                return left + 1

        dfs(root, 0)
        return self.ans
