class Solution:

    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        sorted_freq = sorted(freq.values(), reverse=True)
        return sum([(((i // 8) + 1) * count) for i, count in enumerate(sorted_freq)])
