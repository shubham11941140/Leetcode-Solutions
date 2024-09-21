class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        s = [str(i) for i in range(1, n + 1)]
        s.sort()
        return [int(i) for i in s]
        