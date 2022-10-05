# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def addOneRow(self, root: Optional[TreeNode], val: int,
                  depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        q = [root]
        for _ in range(depth - 2):
            q = [kid for node in q for kid in (node.left, node.right) if kid]
        for node in q:
            node.left = TreeNode(val, node.left)
            node.right = TreeNode(val, None, node.right)
        return root
