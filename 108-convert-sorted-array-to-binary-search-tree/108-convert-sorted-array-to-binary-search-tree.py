# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        n = len(nums)
        return TreeNode(
            nums[n // 2],
            self.sortedArrayToBST(nums[:(n // 2)]),
            self.sortedArrayToBST(nums[(n // 2) + 1:]),
        )
