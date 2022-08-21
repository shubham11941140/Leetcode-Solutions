# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

tree = None


class Codec:

    @staticmethod
    def serialize(root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        global tree
        tree = root
        return ""

    @staticmethod
    def deserialize(data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return tree


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
