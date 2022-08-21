# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def build(self, inn, pre, inStrt, inEnd):
        if inStrt > inEnd:
            return None
        curr = pre[self.preIndex]
        self.preIndex += 1
        tNode = TreeNode(curr)
        if inStrt == inEnd:
            return tNode
        inIndex = self.mp[curr]
        tNode.left = self.build(inn, pre, inStrt, inIndex - 1)
        tNode.right = self.build(inn, pre, inIndex + 1, inEnd)
        return tNode

    def buildTree(self, preorder: List[int],
                  inorder: List[int]) -> Optional[TreeNode]:
        self.mp = {}
        self.preIndex = 0
        n = len(inorder)
        for i in range(n):
            self.mp[inorder[i]] = i
        return self.build(inorder, preorder, 0, n - 1)
