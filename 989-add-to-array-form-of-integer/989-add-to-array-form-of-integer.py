class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = int(''.join([str(i) for i in num]))
        return [int(i) for i in str(n + k)]

