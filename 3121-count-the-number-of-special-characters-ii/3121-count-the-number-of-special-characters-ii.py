class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ll = {}
        fu = {}
        ivd = set()
        for i, ch in enumerate(word):
            letter = ch.lower()
            if ch.islower():
                ll[letter] = i
                # lowercase appeared after uppercase
                if letter in fu:
                    ivd.add(letter)
            else:
                # store only first uppercase occurrence
                if letter not in fu:
                    fu[letter] = i
        return len([1 for letter in ll if letter in fu and letter not in ivd])       