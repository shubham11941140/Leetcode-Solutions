class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        return len({c for c in word if c.isupper()} & {c.upper() for c in word if c.islower()})