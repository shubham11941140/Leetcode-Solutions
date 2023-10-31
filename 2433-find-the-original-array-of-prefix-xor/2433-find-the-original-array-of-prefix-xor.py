class Solution:

    def findArray(self, prefix_xor: List[int]) -> List[int]:
        n = len(prefix_xor)
        original = [0] * n
        original[0] = prefix_xor[0]
        for i in range(1, n):
            original[i] = prefix_xor[i] ^ prefix_xor[i - 1]
        return original
