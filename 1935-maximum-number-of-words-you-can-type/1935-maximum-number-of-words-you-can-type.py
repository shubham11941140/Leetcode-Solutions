class Solution:

    @staticmethod
    def canBeTypedWords(text: str, brokenLetters: str) -> int:
        l = text.split()
        c = 0
        for i in l:
            for j in brokenLetters:
                if j in i:
                    c += 1
                    break
        return len(l) - c
