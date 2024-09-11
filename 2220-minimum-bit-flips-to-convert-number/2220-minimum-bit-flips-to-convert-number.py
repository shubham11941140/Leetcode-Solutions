class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR the two numbers to find differing bits
        xor = start ^ goal
        # Count the number of 1s in the binary representation of xor
        return bin(xor).count('1')        