class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        p = [0] * (n + 1)
        v = ("a", "e", "i", "o", "u")
        for i, w in enumerate(words):
            p[i + 1] = p[i] + int(w[0] in v and w[-1] in v)
        return [p[j[1] + 1] - p[j[0]] for j in queries]