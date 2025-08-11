# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        q = [root]
        for _ in range(depth - 2):
            q = [i for n in q for i in (n.left, n.right) if i]
        for node in q:
            node.left = TreeNode(val, node.left)
            node.right = TreeNode(val, None, node.right)
        return root
