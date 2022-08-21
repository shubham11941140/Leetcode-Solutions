# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # Function to insert Node
    def insert(self, root, item):
        temp = ListNode(0)
        temp.val = item
        temp.next = root
        root = temp
        return root

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        a = []

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                a.append(list1.val)
                list1 = list1.next
            else:
                a.append(list2.val)
                list2 = list2.next

        while list1 is not None:
            a.append(list1.val)
            list1 = list1.next 

        while list2 is not None:
            a.append(list2.val)
            list2 = list2.next      

        root = None
        for i in reversed(range(len(a))):
            root = self.insert(root, a[i])
        return root


