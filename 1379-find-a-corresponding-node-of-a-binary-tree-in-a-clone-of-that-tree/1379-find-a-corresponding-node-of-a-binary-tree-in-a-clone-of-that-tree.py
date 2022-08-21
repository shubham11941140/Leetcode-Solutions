# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def __init__(self):
        self.ans = None

    def find(self, root, item):
        if root.val == item:
            self.ans = root
            return
        if root.left:
            self.find(root.left, item)
        if root.right:
            self.find(root.right, item)

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode,
                      target: TreeNode) -> TreeNode:
        if cloned:
            self.find(cloned, target.val)
        return self.ans
