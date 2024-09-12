class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return len([1 for word in words if all(char in set(allowed) for char in word)])      