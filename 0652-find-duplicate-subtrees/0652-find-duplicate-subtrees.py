# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findDuplicateSubtrees(
            self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.d = defaultdict(int)
        self.res = []
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return "#"
        s = str(root.val) + "," + self.helper(root.left) + "," + self.helper(
            root.right)
        self.d[s] += 1
        if self.d[s] == 2:
            self.res.append(root)
        return s
