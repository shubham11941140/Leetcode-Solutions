class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = Counter()
        for word in words:
            counter += Counter(word)
        n = len(words)
        return all(v % n == 0 for v in counter.values())        