class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        return chr(97 + ((k - 1) & sum(operations[b] << b for b in range((k - 1).bit_length()))).bit_count() % 26)        