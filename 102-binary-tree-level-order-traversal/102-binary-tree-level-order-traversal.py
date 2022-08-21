# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def level(self, root, level):
        if root is None:
            return
        self.ans[level].append(root.val)
        self.level(root.left, level + 1)
        self.level(root.right, level + 1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = [[] for i in range(3000)]
        self.level(root, 0)
        while [] in self.ans:
            self.ans.remove([])
        return self.ans
