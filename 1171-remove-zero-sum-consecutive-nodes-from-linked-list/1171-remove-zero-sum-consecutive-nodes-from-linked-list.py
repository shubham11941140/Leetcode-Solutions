# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        # Initialize prefix sum and a hash map to store the last node with a given prefix sum
        prefix_sum = 0
        hash_map = {0: dummy}

        # Traverse the linked list
        current = head
        while current:
            prefix_sum += current.val
            if prefix_sum in hash_map:
                # Found a zero-sum sequence, remove it
                prev = hash_map[prefix_sum]
                temp = prev.next
                temp_sum = prefix_sum
                while temp != current:
                    temp_sum += temp.val
                    del hash_map[temp_sum]
                    temp = temp.next
                prev.next = current.next
            else:
                hash_map[prefix_sum] = current
            current = current.next

        return dummy.next
