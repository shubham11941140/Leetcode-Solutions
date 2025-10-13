class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]  # result array
        n = len(words)

        # determine if two words are anagrams
        def compare(word1: str, word2: str) -> bool:
            return Counter(word1) == Counter(word2)

        for i in range(1, n):
            if compare(words[i], words[i - 1]):
                continue
            res.append(words[i])
        return res        