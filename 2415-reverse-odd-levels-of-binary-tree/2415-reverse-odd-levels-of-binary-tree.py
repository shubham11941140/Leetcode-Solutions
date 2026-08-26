# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])  # Initialize the queue with root.
        level = 0  # Start with level 0 (root).
        while q:
            # When we are at an odd level, reverse the value of each node in the queue.
            if level % 2:
                l = 0  # left pointer.
                r = len(q) - 1  # right pointer.
                while l < r:
                    # Sweep the value of the left node and right node.
                    q[l].val, q[r].val = q[r].val, q[l].val
                    l += 1
                    r -= 1
            # Same as regular BSF, adding the node for the next level.
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            # Increase the level.
            level += 1
        return root
