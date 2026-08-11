# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        a = [[] for i in range(10**5)]
        q = [(root, 0)]
        while q:
            root, l = q.pop(0)
            a[l].append(root.val)
            if root.left:
                q.append((root.left, l + 1))
            if root.right:
                q.append((root.right, l + 1))
        b = [i for i in a if i]
        n = len(b)
        for i in range(n):
            if i % 2:
                o = b[i]
                if not (
                    o == sorted(o)[::-1] == [j for j in o if not (j % 2)]
                    and len(o) == len(set(o))
                ):
                    return False
            else:
                e = b[i]
                if not (
                    e == sorted(e) == [j for j in e if j % 2] and len(e) == len(set(e))
                ):
                    return False
        return True
