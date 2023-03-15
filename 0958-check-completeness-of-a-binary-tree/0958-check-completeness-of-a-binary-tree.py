# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        while q[0] is not None:
            node = q.pop(0)
            q.append(node.left)
            q.append(node.right)
        while q and q[0] is None:
            q.pop(0)
        return not any(q)      