class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        n = len(word)
        i = 0
        while i < n:
            c = 1
            d = word[i]
            while i + 1 < n and word[i] == word[i + 1] and c < 9:
                i += 1
                c += 1
            comp += str(c) + d
            i += 1
        return comp
                
            

        