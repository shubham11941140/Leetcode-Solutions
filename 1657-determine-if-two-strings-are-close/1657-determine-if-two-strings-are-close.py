class Solution:

    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        d1 = Counter(word1)
        d2 = Counter(word2)
        if set(d1.keys()) != set(d2.keys()):
            return False
        return sorted(d1.values()) == sorted(d2.values())
