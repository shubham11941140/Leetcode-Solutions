# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorder(self, root, a):
        if root is None:
            return
        self.inorder(root.left, a)
        a.append(root.val)
        self.inorder(root.right, a)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        a = []
        self.inorder(root1, a)
        self.inorder(root2, a)
        return sorted(a)
