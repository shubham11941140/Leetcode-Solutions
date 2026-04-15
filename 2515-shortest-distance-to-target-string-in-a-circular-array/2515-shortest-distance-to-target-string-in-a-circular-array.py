class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        return -1 if target not in words else min([min((i - startIndex + n) % n, (startIndex - i + n) % n) for i in range(n) if words[i] == target])