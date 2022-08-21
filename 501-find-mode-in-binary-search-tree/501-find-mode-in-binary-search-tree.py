# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorder(self, root, a):
        if not root:
            return
        self.inorder(root.left, a)
        a.append(root.val)
        self.inorder(root.right, a)

    @staticmethod
    def freq(a):
        d = {}
        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return d

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        a = []
        self.inorder(root, a)
        d = self.freq(a)
        m = max(d.values())
        return [i for i in d if d[i] == m]
