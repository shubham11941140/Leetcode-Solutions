class Solution:

    def minSwaps(self, s: str) -> int:
        unbalanced = 0
        for char in s:
            if char == "[":
                unbalanced += 1
            elif unbalanced > 0:
                unbalanced -= 1
        return (unbalanced + 1) // 2
