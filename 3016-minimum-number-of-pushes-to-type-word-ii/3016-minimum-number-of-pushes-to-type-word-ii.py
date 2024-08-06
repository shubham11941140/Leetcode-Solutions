class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum([(((i // 8) + 1) * count) for i, count in enumerate(sorted(Counter(word).values(), reverse=True))])   