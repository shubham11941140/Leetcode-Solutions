class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if not left:  # if left list is empty
            return n - min(right)
        if not right:  # if right list is empty
            return max(left)
        return max(max(left), n - min(right))
        