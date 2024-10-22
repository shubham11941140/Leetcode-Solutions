# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        level_sums = []
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if len(level_sums) <= level:
                level_sums.append(node.val)
            else:
                level_sums[level] += node.val
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        if k > len(level_sums):
            return -1
        return nlargest(k, level_sums)[-1]
