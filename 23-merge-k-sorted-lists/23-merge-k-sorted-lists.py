# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    @staticmethod
    def toarray(a):
        b = []
        while a is not None:
            b.append(a.val)
            a = a.next
        return b

    @staticmethod
    def insert(root, item):
        temp = ListNode()
        temp.val = item
        temp.next = root
        root = temp
        return root

    def tolist(self, a):
        root = None
        for i in reversed(range(len(a))):
            root = self.insert(root, a[i])
        return root

    def mergeKLists(self,
                    lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        d = []
        for i in lists:
            d += self.toarray(i)
        return self.tolist(sorted(d))
