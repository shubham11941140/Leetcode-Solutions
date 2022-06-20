class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        w = sorted(words, key = len, reverse = True)
        r = []
        for s in w:
            if not any(i.endswith(s) for i in r):
                r.append(s)
        return sum(len(i) + 1 for i in r)