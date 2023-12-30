class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = Counter()
        for word in words:
            counter += Counter(word)
        return all(v % len(words) == 0 for v in counter.values())
