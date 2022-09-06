# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def subtree(self, root):
        if not root:
            return []
        q = [root]
        ans = []
        while q:
            root = q.pop(0)
            ans.append(root.val)
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
        return ans

    def rec(self, root):
        if not root:
            return
        ans = self.subtree(root.left)
        print("f", root.left, ans)
        if 1 not in ans:
            root.left = None
        ans = self.subtree(root.right)
        print("f", root.right, ans)
        if 1 not in ans:
            root.right = None
        self.rec(root.left)
        self.rec(root.right)

    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.rec(root)
        if not root.val:
            if not root.left and not root.right:
                return None
        return root
