# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def cp(self, root):
        if root.left:
            self.p[root.left.val] = root
            self.cp(root.left)
        if root.right:
            self.p[root.right.val] = root
            self.cp(root.right)

    def find(self, root, start):
        # print(18, root.val, start)
        if root.val == start:
            # print(root)
            self.r = root
            return root
        if root.left:
            self.find(root.left, start)
        if root.right:
            self.find(root.right, start)

    def bfs(self, r):
        q = [(r, 0)]
        s = set()
        while q:
            root, level = q.pop(0)

            if not root:
                continue
            if root.val in s:
                continue
            # print(39, root.val, level)
            self.m = max(self.m, level)
            s.add(root.val)
            if root.left:
                q.append((root.left, level + 1))
            # print(38, q)
            if root.right:
                q.append((root.right, level + 1))
            if root.val in self.p:
                q.append((self.p[root.val], level + 1))
            # print(42, q)

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.p = dict()
        self.cp(root)
        # print(self.p)
        r = self.find(root, start)
        # print(61, r, self.r)
        self.m = 0
        self.bfs(self.r)

        return self.m
