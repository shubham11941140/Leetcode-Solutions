class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:        
        return list(set([word1 for i, word1 in enumerate(words) for j, word2 in enumerate(words) if i != j and word1 in word2]))