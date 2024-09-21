class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return [int(j) for j in sorted([str(i) for i in range(1, n + 1)])]        