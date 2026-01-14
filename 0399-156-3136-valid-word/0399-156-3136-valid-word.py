class Solution:

    def isValid(self, word: str) -> bool:
        return bool(match("(?=.*[aeiou])(?=.*[^\daeiou])\w{3,}$", word, I))
