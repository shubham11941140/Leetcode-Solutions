# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a = []
        while head is not None:
            a.append(head.val)
            head = head.next
        print(a)
        n = len(a)
        l = 0
        r = n - 1
        ans = 0
        while l < r:
            s = a[l] + a[r]
            ans = max(ans, s)
            l += 1
            r -= 1
        return ans
            
        