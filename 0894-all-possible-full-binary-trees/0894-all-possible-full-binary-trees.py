# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode(0)]
        res = []
        for i in range(1, n - 1, 2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n - i - 1)
            for l in left:
                for r in right:
                    root = TreeNode(0)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res
